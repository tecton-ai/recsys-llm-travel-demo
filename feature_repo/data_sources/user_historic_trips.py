from tecton import BatchSource, FileConfig

user_historic_trips_batch = BatchSource(
        name='user_historic_trips',
        batch_config=FileConfig(
            uri='s3://travel-data-public-demo/user_historic_trips.parquet',
            file_format='parquet',
            timestamp_field='transaction_timestamp'
    )
)