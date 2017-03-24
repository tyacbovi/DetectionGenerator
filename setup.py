from distutils.core import setup

setup(
    name='DetectionGenerator',
    version='0.1',
    packages=['DetectionGenerator', 'DetectionGenerator.Reporter', 'DetectionGenerator.EntitiesPool',
              'DetectionGenerator.EntityReport', 'DetectionGenerator.DetectionIdGenerator'],
    url='https://github.com/tyacbovi/DetectionGenerator',
    license='',
    author='taly',
    author_email='',
    description='A detection generator tool',
    requires=["simplejson", "plyvel", "confluent_kafka"]
)
