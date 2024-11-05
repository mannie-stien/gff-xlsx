import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def gff_to_xlsx(gff_file, output_xlsx):
    try:
        if not os.path.isfile(gff_file):
            logging.error(f"The file '{gff_file}' does not exist.")
            return

        logging.info("Reading GFF file in chunks...")
        
        with pd.ExcelWriter(output_xlsx, engine='openpyxl') as writer:
            for chunk in pd.read_csv(gff_file, sep='\t', comment='#', header=None,
                                       names=['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes'],
                                       chunksize=10000):
                logging.info(f"Processing chunk with shape {chunk.shape}...")

                # Process attributes
                attributes = chunk['attributes'].str.split(';').apply(lambda x: dict(item.split('=') for item in x if '=' in item))
                attributes_expanded_df = attributes.apply(pd.Series)

                # Combine data
                gff_expanded_df = pd.concat([chunk.drop(columns=['attributes']), attributes_expanded_df], axis=1)

                # Write each chunk to Excel
                # Check if there are already sheets in the writer
                if writer.sheets:
                    startrow = writer.sheets[list(writer.sheets.keys())[-1]].max_row
                else:
                    startrow = 0

                gff_expanded_df.to_excel(writer, index=False, header=startrow == 0, startrow=startrow)

        logging.info(f"Success: GFF file converted to '{output_xlsx}'.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
