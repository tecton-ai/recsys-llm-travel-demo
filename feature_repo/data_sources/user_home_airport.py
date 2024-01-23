from tecton import BatchSource, FileConfig

user_home_airport_batch = BatchSource(
        name='user_home_airport',
        batch_config=FileConfig(
            uri='s3://travel-data-public-demo/user_home_airport.parquet',
            file_format='parquet',
            timestamp_field='last_updated_timestamp'
    )
)