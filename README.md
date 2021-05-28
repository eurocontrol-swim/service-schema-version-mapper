# SWIM Registry Service Description Mapping

This repository can be used as a template to map Service Descriptions written against 
a previous version of the Service Description JSON Schema to a more recent one.

## Usage

### Repl.it

This repository can be used directly in [repl.it](https://repl.it), which provides the user with a pre-configured 
Python environment ready to use. To do so, it suffices to:

1. Create a New repl and choose the option "Import from GitHub" and provide the following URL: [https://github.com/eurocontrol-swim/service-schema-version-mapper](https://github.com/eurocontrol-swim/service-schema-version-mapper)
2. Click the blue button "Import from GitHub".
3. When the repository finishes loading into the repl.it environment you can click the "Run ▶" button which will execute the *mapping.py* script. The first time it runs it will automatically install some dependencies.

Optional:

- You can tune which input or output file to use in the *mapping.py* file by simply editing the variables *input_file_path* and *output_file_path*.
- You can add new Service Description Files into the *input* folder which you can then point to in the *mapping.py* script by changing appropriately the *input_file_path* variable.
- You can fine-tune the mapping performed by the script by editing the *jsonize-mapping.json* file which contains the rules applied by the mapping. To read more about how the mapping works behind the scene you can check the following Python library: [Jsonize](https://github.com/eurocontrol-swim/jsonize)