# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/asm-attack-signatures/availability' resources
# =============================================


class Live_updateAsmattacksignaturesAvailabilitySchema(MetaParser):

    schema = {}


class Live_updateAsmattacksignaturesAvailability(
    Live_updateAsmattacksignaturesAvailabilitySchema
):
    """ To F5 resource for /mgmt/tm/live-update/asm-attack-signatures/availability
    """

    cli_command = "/mgmt/tm/live-update/asm-attack-signatures/availability"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
