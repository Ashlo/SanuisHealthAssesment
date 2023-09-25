import config
from business_logic import data_ingestion, data_cleaning, data_visualisation, data_aggregation, data_output

def main():
    try:
        df = data_ingestion.load_data(config.INPUT_PATH)
        df_cleaned = data_cleaning.clean_data(df)
        kpi_1 = data_aggregation.heart_rate_kpi(df_cleaned)
        kpi_2 = data_aggregation.temp_variability(df_cleaned)
        kpi_3 = data_aggregation.act_intensity(df_cleaned)
        data_output.save_data(kpi_1, config.OUTPUT_PATH_KPI_1,'heart_rate_KPI.csv')
        data_output.save_data(kpi_2,config.OUTPUT_PATH_KPI_2,'temp_variability.csv')
        data_output.save_data(kpi_3,config.OUTPUT_PATH_KPI_3,'act_intensity.csv')
        data_visualisation.save_report(config.HEART_RATE_CSV, config.TEMP_VARIABLILITY_CSV, config.ACT_INTENSITY_CSV)
    except Exception as e:
        print(f'Error occured {e}')
        raise

if __name__ == '__main__':
    main()
