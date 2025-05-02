from modules.configuration.config import DISTRIBUTION_CENTERS


def getDistributionCenterName(distribution_center_id):
    """Returns the name of the distribution center based on its ID."""
    return DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT.get(
        str(distribution_center_id), "Unknown Distribution Center"
    )
