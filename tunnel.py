# from sshtunnel import SSHTunnelForwarder
#
# EC2_URL = 'ec2-13-125-100-207.ap-northeast-2.compute.amazonaws.com'
# KEY_PATH = 'tonetwork_reservation.pem'
# BASE_URL = "https://sonoapi.traveland.co.kr"
#
# ssh_tunnel = SSHTunnelForwarder(
#     (EC2_URL, 22),
#     ssh_username='ubuntu',  # I used an Ubuntu VM, it will be ec2-user for you
#     ssh_pkey=KEY_PATH,  # I had to give the full path of the keyfile here
#     remote_bind_address=(BASE_URL, 8000),
#     local_bind_address=('127.0.0.1', 8088)
# )
#
