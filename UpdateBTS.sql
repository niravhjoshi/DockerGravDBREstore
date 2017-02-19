
#####################################################
# Now preparing for DB to be update rows
#####################################################


############################################################
# Updating values for appnode and backoffice node to 127.0.0.1
############################################################

update bts.graconfiguration set propValue = "127.0.0.1" where propKey in ('APPLICATION-NODE', 'BACKOFFICE-NODE');


##########################################################################
# Updating values for servicebridge.url node to http://host:80/servicebridge
##########################################################################

update bts.graConfiguration set propvalue = 'http://host:80/servicebridge' where propkey like 'servicebridge.url';


##########################################################################
# Updating values for tags.url node to http://host:80/tags
##########################################################################

update bts.graConfiguration set propvalue = 'http://host:80/tags' where propkey like 'tags.url';

##########################################################################
# Delete graversion table form bts databases
##########################################################################

delete from bts.graversion;


##########################################################################
# Update kettle configuration to point to localhost in Win Dev Instance.
##########################################################################

UPDATE `comparedb`.`cc_accesscontrol` SET `accessURL`='http://localhost:80/admin/kettle/' WHERE `accessControl_Id`='1';