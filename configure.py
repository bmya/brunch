import os
import subprocess
import yaml


try:
    with open('dependencies.yml', 'r') as f:
        config = yaml.load(f)
except:
    print """

    ERROR: could not read dependencies file"""

addons_path = 'addons_path = ' + config['docker_addons_root'] + ','
lines_seen = set() # holds lines already seen
outfile = open('requirements.txt', "w")

for module in config['submodules']:
    for k, v in module.iteritems():
        addons_path += config['docker_addons_root'] + '/' + k + ','
        # line = 'git clone -b {} {} {}'.format(v['branch'], v['origin'], k)
        line = 'git submodule add -b {} {} {}'.format(v['branch'], v['origin'], k)
        print line
        try:
            subprocess.call(line, shell=False)
        except:
            print 'ya existe'
        try:
            print 'leyendo archivo de requerimientos en {}'.format(k)
            for line in open(k + '/requirements.txt', 'r'):
                if line not in lines_seen:  # not a duplicate
                    outfile.write(line)
                    lines_seen.add(line)
        except:
            print 'no hay archivo de requerimientos en {}'.format(k)

outfile.close()

print
print 'introduzca en odoo.conf la siguiente linea de addons_path'
print addons_path[:-1]
# addons_path = /mnt/extra-addons,/mnt/extra-addons/oca-queue,/mnt/extra-addons/oca-reporting-engine,/mnt/extra-addons/oca-connector,/mnt/extra-addons/oca-product-attribute,/mnt/extra-addons/oca-partner-contact,/mnt/extra-addons/oca-account-financial-tools,/mnt/extra-addons/ingadhoc-miscellaneous,/mnt/extra-addons/ingadhoc-account-financial-tools,/mnt/extra-addons/ingadhoc-account-payment,/mnt/extra-addons/ingadhoc-odoo-argentina,/mnt/extra-addons/oca-account-payment,
