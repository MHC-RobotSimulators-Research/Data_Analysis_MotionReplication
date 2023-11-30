class ReadFileName:
    def __init__(self, file_name=None, mode=None, raven_type=None):
        self.file_name = file_name
        self.mode = mode
        self.raven_type = raven_type
        if self.mode == None and raven_type == None:
            self.parse_file_name()
        
        # if self.raven_type == None and self.mode != None:

    def set_file_name(self):
        self.file_name = "raven_data/" + self.mode + "_" + self.raven_type + ".csv"

    def parse_file_name(self):
        # Find the second dash
        slash_index = self.file_name.find('/')
        first_dash_index = self.file_name.find('/')
        second_dash_index = self.file_name.find('_', first_dash_index + 1)
        third_dash_index = self.file_name.find('_', second_dash_index + 1)

        # Extract the mode and raven type from the file name
        if slash_index != -1 and second_dash_index != -1:
            # set self.mode
            self.mode = self.file_name[slash_index+1:third_dash_index]
            # set self.raven_type
            self.raven_type = self.file_name[third_dash_index + 1:self.file_name.find('.csv')]

    def get_mode(self):
        return self.mode

    def get_raven_type(self):
        return self.raven_type


# Example usage:
file_name = "raven_data/twoarm_p5_phys1.csv"
reader = ReadFileName(file_name)
mode = reader.get_mode()
raven_type = reader.get_raven_type()

print("Mode:", mode)
print("Raven Type:", raven_type)
