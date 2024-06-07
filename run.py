# Import core Waitress functionality
from waitress import serve


# Import your Flask applications
from app import app1
from etl import app2
from home import home

# Import Composite to create a URL map
from paste.urlmap import URLMap

# Set debug mode
app1.debug = True
app2.debug = True
home.debug = True

# Define mount points for each application
url_map = URLMap()
url_map['/'] = home
url_map['/app1'] = app1
url_map['/app2'] = app2

# Start the Waitress server with mount points
serve(url_map, listen='*:8888')  # Adjust port as needed
