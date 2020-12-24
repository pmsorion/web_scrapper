import argparse
import logging
logging.basicConfig(level=logging.INFO)

from common import config

logger = logging.getLogger(__name__)


def _jobs_scraper(job_site_uid):
    host = config()['job_site'][job_site_uid]['url']

    logging.info('Beginning scraper fro {}'.format(host))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    jobs_site_choices = list(config()['job_site'].keys())

    parser.add_argument('job_site',
                        help='The jobs site that you want to scrape',
                        type=str,
                        choices=jobs_site_choices)

    args = parser.parse_args()
    _jobs_scraper(args.job_site)