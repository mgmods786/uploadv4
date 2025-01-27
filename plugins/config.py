import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7711740007:AAGMeiEzZIa-MKJhPALh_0-MhFEG4lH1Flc")
    
    API_ID = int(os.environ.get("API_ID", "22216618"))
    
    API_HASH = os.environ.get("API_HASH", "cb9b9fd32dde8a17b8e55b8131b08ae5")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = ""
    
    FREE_USER_MAX_FILE_SIZE = 2097152000

    MAX_SPLIT_SIZE = 4187407334
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    DEF_WATER_MARK_FILE = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mgmods786:<db_@Teenwolf786>@cluster0.0owje.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002294720790"))
    
    LOGGER = logging
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "7711740007"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "file2linkbg_bot")
                                  
