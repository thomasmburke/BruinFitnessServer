import logging
from datetime import datetime as dt
from datetime import timedelta
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

DEFAULT_CLASSES = {
    'Monday': 
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:30am - 8:30am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:30pm - 5:30pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:15pm - 8:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:30am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00am - 8:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '1:00pm - 2:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '2:00pm - 3:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:00pm - 5:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00pm - 8:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Tuesday': 
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:30am - 8:30am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:30pm - 5:30pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:15pm - 8:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:30am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00am - 8:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '1:00pm - 2:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '2:00pm - 3:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:00pm - 5:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00pm - 8:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Wednesday': 
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:30am - 8:30am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:30pm - 5:30pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:15pm - 8:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:30am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00am - 8:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '1:00pm - 2:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '2:00pm - 3:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:00pm - 5:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00pm - 8:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Thursday': 
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:30am - 8:30am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:30pm - 5:30pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:15pm - 8:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:30am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00am - 8:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '1:00pm - 2:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '2:00pm - 3:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:00pm - 5:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00pm - 8:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Friday': 
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:30am - 8:30am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:30pm - 5:30pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:15pm - 8:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:30am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00am - 7:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00am - 8:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '12:00pm - 1:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '1:00pm - 2:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '2:00pm - 3:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '3:00pm - 4:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '4:00pm - 5:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '6:00pm - 7:00pm',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '7:00pm - 8:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Saturday':
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:15am - 12:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
    ],
    'Sunday':
    [
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Weightlifting'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:15am - 12:15pm',
            'workoutType': 'Metcon'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '8:00am - 9:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '9:00am - 10:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '10:00am - 11:00am',
            'workoutType': 'Open Gym'
        },
        {
            'reservationCnt': 0,
            'reservedUsers': [],
            'time': '11:00am - 12:00pm',
            'workoutType': 'Open Gym'
        },
    ]
}

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

def get_first_day_of_next_month(anyDatetime) -> "datetime.datetime":
    """
    Summary: Gets the first day of next month based off current datetime
    """
    return (anyDatetime.replace(day=1) + timedelta(days=32)).replace(day=1)

def daterange(startDate: "datetime.datetime", endDate: "datetime.datetime"):
    """
    Summary: Generator function used to hide/abstract the iteration over date ranges
    """
    for n in range(int((endDate - startDate).days)):
        yield startDate + timedelta(n)

def send_error_msg(db, subject, html):
    """
    Summary: Sends an email to my account if an error/warning is encountered in the process
    """
    db.collection('errors').add({
        "to": "tburke@bu.edu",
        "message": {
            "subject": subject,
            "html": html
        }
    })

def add_classes(event, context):
    """
    Summary: Writes next month's classes (with empty reservations) to Firestore.
    """
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         event (dict):  The dictionary with data specific to this type of
         event. The `data` field contains the PubsubMessage message. The
         `attributes` field will contain custom attributes if there are any.
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata. The `event_id` field contains the Pub/Sub message ID. The
         `timestamp` field contains the publish time.
    """
    #TODO: Have this run on the 20th of every month. (Cloud Scheduler -> PubSub -> GCF)?
    db = initialize_firestore_client()

    # Get start and end dates to populate classes for
    # startDate: first day of next month
    startDate = get_first_day_of_next_month(dt.today())
    startDateString = startDate.strftime('%Y-%m-%d')
    # endDate first day of the month after startDate
    endDate = get_first_day_of_next_month(startDate)
    logger.info(f"startDate: {startDate.strftime('%Y-%m-%d')}")
    logger.info(f"endDate: {endDate.strftime('%Y-%m-%d')}")

    # Check if a document exists under the start date of next month's class schedule
    docExists = db.collection(f'schedules/Redwood City/dates/{startDateString}/classes').limit(1).get()
    # If it does exist no need to add the classes again
    if docExists:
        logger.warning('classes have already been added, so no writes will occur to avoid contamination..')
        # Send email alert as this is unexpected
        send_error_msg(db=db, subject="GCF:add_classes: No classes added because some were already detected",
        html=f"No classes were added for the month of {startDateString}<br />This is likely the cron that runs mid month. I suggest seeing if any classes were created and creating them if not.")
    # If no doc exists we'll assume it is safe to classes for next month
    else:
        # Iterate through each date in the month
        for classDate in daterange(startDate, endDate):
            classDateString = classDate.strftime("%Y-%m-%d")
            dayOfWeek = classDate.strftime('%A')
            logger.info(f'writing class data for classDate: {classDateString}')
            logger.info(f"classDate day of week: {dayOfWeek}")
            # Add each class for the day separately as they all have their own reservationCnt
            # TODO: wrap this in a try, except and send a notification in case something doesn't work as expected
            for defaultClass in DEFAULT_CLASSES[dayOfWeek]:
                # retry writing Firestore document 10 times upon failure
                for i in range(0,10):
                    try:
                        # if write is successful move on to next doc
                        db.collection(f'schedules/Redwood City/dates/{classDateString}/classes').add(defaultClass)
                        break
                    except Exception as e:
                        # if write is unsuccessful then we will iterate until we failed 10 times
                        # in which case we raise an exception and halt the process.
                        logger.error(f"error writing class document: {e}")
                        # retry document write
                        if i == 9:
                            send_error_msg(db=db,subject="GCF:add_classes: Error writing class", 
                            html=f"document failed to be added for {classDate}<br />The document that failed to be added contained the following content<br />{defaultClass}")
                            raise e
                        continue
    


if __name__ == "__main__":
    add_classes()

