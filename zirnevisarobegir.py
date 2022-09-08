from babelfish import Language
from subliminal import download_best_subtitles, region, save_subtitles, scan_videos
import os
from dotenv import load_dotenv

load_dotenv()
region.configure('dogpile.cache.dbm', arguments={'filename': 'cachefile.dbm'})
videos = scan_videos(os.getcwd())
subtitles = download_best_subtitles(videos, {Language('eng'), Language('fas')},
        providers=['opensubtitles'], provider_configs={'opensubtitles':
            {'username': os.getenv('OPENSUBTITLES_USERNAME'), 'password': os.getenv('OPENSUBTITLES_PASSWORD')}})
for v in videos:
    print(v)
    print(subtitles[v])
    save_subtitles(v, subtitles[v])

