import pandas as pd

from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
from utils.constants import CLIENT_ID, SECRET, OUTPUT_PATH

def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    #Connecting to reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'pthk_nikesh')

    #extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    df = pd.DataFrame(posts)

    # transformation
    df = transform_data(df)

    #loading_to_csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(df, file_path)

    return file_path