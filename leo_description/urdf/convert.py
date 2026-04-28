from xacrodoc import XacroDoc
# Load the Xacro file
doc = XacroDoc.from_file("macros.xacro")
# Convert to a string of URDF
urdf_str = doc.to_urdf_string()
# Write to a file
doc.to_urdf_file("macros.urdf")