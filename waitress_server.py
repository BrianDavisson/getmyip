from waitress import serve
import getmyip
serve(getmyip.app, host='0.0.0.0', port=5002)