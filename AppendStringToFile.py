class AppendStringToFile(object):
    """
        AppendStringToFile Class Description:
        Appends a new line to the file with specific
        name as filename
        """

    def __init__(self):
        print('In AppendStringToFile')
        """self.filePatheName = file_path_name
        self.newstring = newstring
        self.rowcount = rowcount"""

    def to_file(self, file_path_name, newstring, rowcount):

        with open(file_path_name, 'a') as f:
            f.write(newstring)

        rowcount += 1
        return self.rowcount
