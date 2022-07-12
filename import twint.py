import twint

# Configure
c = twint.Config()
c.Username = "nickgerli1"
c.Search = "recession"
c.Output = "tweets.csv"
c.Store_csv = True

# Run
twint.run.Search(c)
