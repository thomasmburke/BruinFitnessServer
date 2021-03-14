import logging
from os.path import abspath, dirname, join

from google.cloud import firestore
from google.oauth2 import service_account

# Set logger
logger = logging.getLogger(__name__)

# Set default logging level
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
    datefmt='%Y-%m-%dT%H:%M:%S')

def initialize_firestore_client() -> "class google.cloud.firestore_v1.client.Client":
    """
    Summary: Initializes Firestore Client using either GOOGLE_APPLICATION_CREDENTIALS or service account key
    Raises: 
        Exception: Couldn't initialize Firestore Client
    """
    try:
        logger.info('trying to initialize firestore client via service account key...')
        parentDir = dirname(dirname(abspath(__file__)))
        logger.info(f'parentDir: {parentDir}')
        serviceAccountKeyFile = join(parentDir, 'creds/bruinfitnessprod-firebase-adminsdk.json')
        logger.info(f'serviceAccountKeyFile: {serviceAccountKeyFile}')
        credentials = service_account.Credentials.from_service_account_file(
        '../creds/bruinfitnessprod-firebase-adminsdk.json')
        return firestore.Client(credentials=credentials)
    except:
        try:
            logger.info('trying to initialize firestore client via GOOGLE_APPLICATION_CREDENTIALS...')
            return firestore.Client()
        except:
            logger.error("Couldn't initialize firestore client via Service Account key nor GOOGLE_APPLICATION_CREDENTIALS")
            raise Exception("Couldn't initialize firestore client via Service Account key nor GOOGLE_APPLICATION_CREDENTIALS")
    
db = initialize_firestore_client()
collectionRef = db.collection('constants').add({'test': 'testvalue'})
