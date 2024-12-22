print("OE: 3")
class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        
        return f"{self.username} logged in"

    def post(self, content):
        
        return f"Posted: {content}"
    
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self, story_content):
        
        return f"Story shared: {story_content}"
class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        
        return f"Tweeted: {tweet_content}"

instagram_account = InstagramAccount("user123", "pass123", 1500)
twitter_account = TwitterAccount("user456", "pass456", 300)


print(instagram_account.login())  
print(instagram_account.post("New post on Instagram"))  
print(twitter_account.login())  
print(twitter_account.post("New post on Twitter"))  

    
print(instagram_account.share_story("Check out my new story!"))  
print(twitter_account.tweet("Hello Twitter!"))
