from setuptools import setup, Extension
import sysconfig

# Get the correct include directory for the active Python
python_include = sysconfig.get_path('include')

# Create extension with correct paths
rdrand_ext = Extension(
    '_rdrand',
    sources=['rdrand.c'],
    include_dirs=[python_include],
)

setup(
    ext_modules=[rdrand_ext],
)
