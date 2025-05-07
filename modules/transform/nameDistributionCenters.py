from modules.configuration.ordersConfig import DISTRIBUTION_CENTERS


"""
Uses distribution centers dict setted in config and loaded in extraction
to return the name of the distribution center based on its ID.
"""


def getDistributionCenterName(distribution_center_id):
    return DISTRIBUTION_CENTERS.DISTRIBUTION_CENTERS_DICT.get(
        str(distribution_center_id), "Unknown Distribution Center"
    )
