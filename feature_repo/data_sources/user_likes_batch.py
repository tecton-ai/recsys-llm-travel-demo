from tecton import BatchSource, FileConfig

user_likes_batch = BatchSource(
        name='user_likes_batch',
        batch_config=FileConfig(
            uri='s3://travel-data-public-demo/user_likes.parquet',
            file_format='parquet',
            timestamp_field='last_updated_timestamp'
    )
)