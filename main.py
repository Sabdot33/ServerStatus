from flask import Flask, render_template, request
from Samba import check_smbd_service_status
from Jellyfin import check_jellyfin_service_status
from Xrdp import check_xrdp_service_status
from getcustomservicedata import getServiceStatus
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def GetStatuses():
    """Checks the Samba service status and returns a dictionary."""
    SambaService = check_smbd_service_status()
    JellyfinService = check_jellyfin_service_status()
    XrdpService = check_xrdp_service_status()
    return render_template("index.html", 
                            SambaService=SambaService,
                            JellyfinService=JellyfinService,
                            XrdpService=XrdpService
                            )
    
@app.route('/customservice', methods=['GET', 'POST'])
def customservice():
    servicename = request.form.get('service_name')
    ServiceData = getServiceStatus(servicename)
    return render_template("customservice.html", 
                           CustomServiceStatus=ServiceData, 
                           servicename=servicename
                           )
    
if __name__ == "__main__":
  serve(app, host="0.0.0.0", port=5000)
  
