import logging
import os
import subprocess

# Set logger
logger = logging.getLogger(__name__)


def deploy_gcf() -> "int":
    """
    Summary: Redeploys the GCF
    """
    logger.info('deploying Google Cloud Function...')
    filePath = os.path.dirname(os.path.realpath(__file__))
    deployPath = os.path.join(filePath, "src/")
    return subprocess.call(args=f"gcloud functions deploy add-classes --entry-point add_classes --runtime python38 --trigger-topic mfp-1-topic --timeout 540s --project {os.getenv('BRUIN_FITNESS_PROJECT_ID')}".split(" "), cwd=deployPath)


if __name__ == '__main__':
    deploy_gcf()
