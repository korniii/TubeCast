import pafy

playlist = pafy.get_playlist("PLpaD0ybYH0S3XOMnC8ADVycFyEcjRJ6Aj")
videos = playlist['items']


for video in videos:
  p = video['pafy']
  print(p.title)
  best = p.getbestaudio()
  print(best.url)
