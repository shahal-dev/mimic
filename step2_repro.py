import os
import json

config = json.load(open('config.json'))
config["info_dict"]["obs_ids"] = []
for folder in os.listdir(config["info_dict"]["cluster_directory"]):
    obs_id = folder.split()[0]
    config["info_dict"]["obs_ids"].append(obs_id)
script_dir = f'./parent/{config["info_dict"]["name"]}/scripts'
with open('config.json', 'w') as f:
    json.dump(config, f, indent=4)

os.makedirs(script_dir, exist_ok=True)
#script1: preprocess the data with chandra_repro
script1 = open(os.path.join(script_dir, 'preprocess_data.sh'), 'w')
script1.write(f'cd {config["info_dict"]["cluster_directory"]}\n')
script1.write('conda activate ciao\n')

for obs_id in config["info_dict"]["obs_ids"]:
    script1.write(f'rm -rf {config["info_dict"]["parent_directory"]}/reprocessed_data/{obs_id}\n')
    mode_obs_id = os.popen('dmkeypar '+ config["info_dict"]["cluster_directory"]+ "/" + obs_id +'/primary/*evt2.fits.gz DATAMODE echo+').read().split()[0]
    if mode_obs_id == 'VFAINT':
        script1.write(f'chandra_repro {obs_id} check_vf_pha=yes verbose=1 outdir = ../{config["info_dict"]["parent_directory"]}/{config["info_dict"]["name"]}/reprocessed_data/{obs_id} clobber = yes\n')
    else:
        script1.write(f'chandra_repro {obs_id} verbose=1 outdir = ../{config["info_dict"]["parent_directory"]}/{config["info_dict"]["name"]}/reprocessed_data/{obs_id} clobber = yes\n')

    script1.write('punlearn ardlib\n')

script1.close()

#script2: auto deflaring point sources
script2 = open(os.path.join(script_dir, 'deflare_point_sources.sh'), 'w')
script2.write(f'cd {config["info_dict"]["parent_directory"]}/reprocessed_data\n')
script2.write('conda activate ciao\n')

# for folder in os.listdir(config['info_dict']['parent_directory'] + '/' + config['info_dict']['name'] + '/reprocessed_data'):
