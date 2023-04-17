from instapy import InstaPy

session = InstaPy(username="{username}", password="{password}")
session.set_quota_supervisor(enabled=True, peak_comments_daily=200, peak_comments_hourly=22)
session.set_relationship_bounds(enabled=True, max_followers=8500)
session.set_use_clarifai(enabled=True, api_key='04d37450fe654234b5fa6581bcef4d80')
session.clarifai_check_img_for(['nsfw'])
session.like_by_tags(["Books", "Kindle", "book", "amazonkindle","ebook","booklover","booklovers","bookslover","bookslovers","kindlebook","pdf","bookreviewer","bookreview","bookreviews","goodbook","amazingbook","greatbook","greatbooks","bibliophile","bookish","bookworm"], amount=200)
session.set_dont_like(["naked", "nsfw"])
session.set_do_follow(True, percentage=100)
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice!", "Awesome!", "Amazing", "Cool", "Wow", "Good"])
session.login()
session.end()