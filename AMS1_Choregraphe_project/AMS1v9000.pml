<?xml version="1.0" encoding="UTF-8" ?>
<Package name="AMS1v9000" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
    </Dialogs>
    <Resources>
        <File name="estuunrobot" src="behavior_1/estuunrobot.wav" />
        <File name="pepper" src="pepper.zip" />
        <File name="ams1v2-3c3142-0.0.0" src="ams1v2-3c3142-0.0.0.pkg" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="ExampleDialog_frf" src="behavior_1/ExampleDialog/ExampleDialog_frf.top" topicName="ExampleDialog" language="fr_FR" />
    </Topics>
    <IgnoredPaths />
</Package>
