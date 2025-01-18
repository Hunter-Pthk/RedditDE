def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    #Connecting to reddit instance
    instance = connect_reddit(ÇLIENT_ID, SECRET, 'Airscholar Agent')