from instapy import InstaPy

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder


# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")

InstaPy(username="praisingofcars", password="clubmate123", browser='chrome')\
  .login()\
  .set_upper_follower_count(limit = 2500) \
  .like_by_tags(['car', '#tuning'], amount=10) \
  .end()
