from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos
import os

region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
videos = scan_videos(os.getcwd())
subtitles = download_best_subtitles(videos, {Language('eng'), Language('fas')})
for v in videos:
    print(v)
    save_subtitles(v, subtitles[v])

