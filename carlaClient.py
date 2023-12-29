import carla
import random 

client = carla.Client('localhost', 2000)
world = client.get_world()

# Loading a map 
client.load_world("Town05")

# SPECTATOR NAVIGATION
'''spectator = world.get_spectator() 

transform = spectator.get_transform()

location = transform.location
rotation = transform.rotation

spectator.set_transform(carla.Transform())'''

# ADDING NPCs 

vehicle_blueprints = world.get_blueprint_library().filter('*vehicle*')

spawn_points = world.get_map().get_spawn_points()

# Spawning 10 vehicles 
for i in range(0, 50):
    world.try_spawn_actor(random.choice(vehicle_blueprints), random.choice(spawn_points))


# EGO VEHICLE 
'''
spawn_points = world.get_map().get_spawn_points()
    
ego_bp = world.get_blueprint_library().find("vehicle.lincoln.mkz_2020")
ego_bp.set_attribute('role_name', 'hero')
ego_vehicle = world.spawn_actor(ego_bp, random.choice(spawn_points))

# Attaching camera sensor to ego vehicle 
camera_init_trans = carla.Transform(carla.Location(z=1.5)) # Camera on top of the vehicle
camera_bp = world.get_blueprint_library().find('sensor.camera.rgb')
camera = world.spawn_actor(camera_bp, camera_init_trans, attach_to = ego_vehicle)

# Using the camera to record 
camera.listen(lambda image: image.save_to_disk('out/%06d.png' % image.frame))
'''

# Animating the traffic 
for vehicle in world.get_actors().filter("*vehicle*"): 
    vehicle.set_autopilot(True)
