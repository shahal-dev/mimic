import os
import json

filename = "config.json"

config = {
    'info_dict': {},
    'flags': {},
}

inp = input("Do you want to start from scratch? (y/n): ")
if inp == 'y':
    name = input("Enter the name of the cluster(e.g. Perseus): ")
    sn_per_region = int(input("Enter the number of SNs per region(e.g. 10): "))
    reg_smoothness = float(input("Enter the smoothness of the regions(e.g. 0.1): "))
    cluster_directory = input('Enter the directory path for the downloaded data(e.g. /path/to/cluster_data): ') 
    parent_directory = input('Enter the directory path for the parent directory(e.g. /path/to/parent_directory): ')

    config['info_dict']['name'] = name
    config['info_dict']['sn_per_region'] = sn_per_region
    config['info_dict']['reg_smoothness'] = reg_smoothness
    config['info_dict']['cluster_directory'] = cluster_directory
    config['info_dict']['parent_directory'] = parent_directory

    parent_directory = os.path.join(parent_directory, name)
    if not os.path.exists(parent_directory):
        os.makedirs(parent_directory)

    reppro_dir = os.mkdir(os.path.join(parent_directory, 'reprocessed_data'))
    merge_dir = os.mkdir(os.path.join(parent_directory, f'merge_{name}_{reg_smoothness}_{sn_per_region}'))
    spec_file_dir = os.mkdir(os.path.join(parent_directory, 'spec_files'))
    region_file_dir = os.mkdir(os.path.join(parent_directory, 'region_files'))
    map_file_dir = os.mkdir(os.path.join(parent_directory, 'map_files'))


    with open(filename, 'w') as f:
        json.dump(config, f, indent=4)
else:
    with open(filename, 'r') as f:
        info_dict = json.load(f)   
    parent_directory = info_dict['parent_directory']
    name = info_dict['name']
    sn_per_region = info_dict['sn_per_region']
    reg_smoothness = info_dict['reg_smoothness']
    cluster_directory = info_dict['cluster_directory']

    reppro_dir = os.path.join(parent_directory, 'reprocessed_data')
    merge_dir = os.path.join(parent_directory, f'merge_{name}_{reg_smoothness}_{sn_per_region}')
    spec_file_dir = os.path.join(parent_directory, 'spec_files')
    region_file_dir = os.path.join(parent_directory, 'region_files')
    map_file_dir = os.path.join(parent_directory, 'map_files')

    if not os.path.exists(reppro_dir):
        os.makedirs(reppro_dir)
    if not os.path.exists(merge_dir):
        os.makedirs(merge_dir)
    if not os.path.exists(spec_file_dir):
        os.makedirs(spec_file_dir)
    if not os.path.exists(region_file_dir):
        os.makedirs(region_file_dir)
    if not os.path.exists(map_file_dir):
        os.makedirs(map_file_dir)




config['flags']['reprocessed'] = False
config['flags']['flare_filtered'] = False
config['flags']['merge_data'] = False
config['flags']['flux_maps'] = False
config['flags']['remove_point_source'] = False
config['flags']['countour_binning'] = False
config['flags']['convert_region_coordinates'] = False
config['flags']['extract_spectra'] = False
config['flags']['xspec_fitting'] = False
config['flags']['parse_results'] = False
config['flags']['maps_created'] = False

with open(filename, 'w') as f:
    json.dump(config, f, indent=4)





print(f"Cluster information saved to {filename}")
