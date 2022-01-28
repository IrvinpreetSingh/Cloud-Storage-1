import dropbox
class UploadFiles :
    def __init__ (self,acess_token):
        self.acess_token = acess_token
    def uploadFile(self,FileFrom,FileTo):
        dbx = dropbox.Dropbox(self.acess_token)
        f = open(FileFrom,'rb')
        dbx.files_upload(f.read(),FileTo)
def main():
    acess_token = 'DFWHI-z_XtsAAAAAAAAAAfYVY0yvOpJb85eInCb5KdT9OESAZ9y-E2c2hmpFzAr0'
    data =  UploadFiles(acess_token)
    FileFrom = input("Type your file path here :")
    FileTo = input("Type path to upload files :")
    data.uploadFile(FileFrom,FileTo)
    print("Sucessfully Uploaded")
main()

