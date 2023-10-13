# Class for the Duet Printer
# This class will be used to control the Duet Printer
# Set up methods to send gcode to the printer
import requests


class DuetPrinter:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.url = "http://" + self.ip_address + ":80"
        self.gcode = ""

    # method to send gcode to printer
    def send_gcode(self, gcode):
        self.gcode = gcode
        # send gcode to printer
        r = requests.post(self.url + "/rr_gcode", data=self.gcode)
        # return success or failure
        return "success"