import pandas

class WQXMapper:

    # WQX semantic names (as developed for use as tabular column headings) that occur in WQX-Outbound messages
    wqx_semantic_names = {
        'DrainageAreaMeasure/MeasureUnitCode',
        'MonitoringLocationTypeName',
        'LongitudeMeasure',
        'AquiferName',
        'HorizontalCoordinateReferenceSystemDatumName',
        'HorizontalAccuracyMeasure/MeasureValue',
        'HUCEightDigitCode',
        'LatitudeMeasure',
        'DrainageAreaMeasure/MeasureValue',
        'StateCode',
        'OrganizationFormalName',
        'WellDepthMeasure/MeasureUnitCode',
        'OrganizationIdentifier',
        'CountyCode',
        'HorizontalCollectionMethodName',
        'MonitoringLocationIdentifier',
        'MonitoringLocationName',
        'ContributingDrainageAreaMeasure/MeasureValue',
        'MonitoringLocationDescriptionText',
        'CountryCode',
        'VerticalMeasure/MeasureValue',
        'VerticalMeasure/MeasureUnitCode',
        'VerticalAccuracyMeasure/MeasureUnitCode',
        'ConstructionDateText',
        'VerticalAccuracyMeasure/MeasureValue',
        'VerticalCoordinateReferenceSystemDatumName',
        'VerticalCollectionMethodName',
        'WellHoleDepthMeasure/MeasureUnitCode',
        'AquiferTypeName',
        'FormationTypeText',
        'HorizontalAccuracyMeasure/MeasureUnitCode',
        'ContributingDrainageAreaMeasure/MeasureUnitCode',
        'WellHoleDepthMeasure/MeasureValue',
        'SourceMapScaleNumeric',
        'WellDepthMeasure/MeasureValue',
        'ActivityIdentifier',
        'PrecisionValue',
        'SampleAquifer',
        'StatisticalBaseCode',
        'ActivityStartTime/Time',
        'ResultDetectionConditionText',
        'ActivityStartDate',
        'SampleTissueAnatomyName',
        'ActivityBottomDepthHeightMeasure/MeasureUnitCode',
        'AnalysisStartDate',
        'DetectionQuantitationLimitTypeName',
        'SampleCollectionMethod/MethodName',
        'ResultTemperatureBasisText',
        'ResultDepthHeightMeasure/MeasureValue',
        'ResultParticleSizeBasisText',
        'USGSPCode',
        'ActivityTypeCode',
        'MeasureQualifierCode',
        'ResultDepthAltitudeReferencePointText',
        'ActivityDepthAltitudeReferencePointText',
        'ResultCommentText',
        'ActivityTopDepthHeightMeasure/MeasureUnitCode',
        'ResultValueTypeName',
        'ActivityTopDepthHeightMeasure/MeasureValue',
        'ResultLaboratoryCommentText',
        'ActivityEndTime/TimeZoneCode',
        'ResultMeasure/MeasureUnitCode',
        'ActivityCommentText',
        'ResultDepthHeightMeasure/MeasureUnitCode',
        'ActivityEndDate',
        'HydrologicEvent',
        'SampleCollectionMethod/MethodIdentifier',
        'ActivityMediaSubdivisionName',
        'ActivityDepthHeightMeasure/MeasureUnitCode',
        'CharacteristicName',
        'ResultAnalyticalMethod/MethodIdentifierContext',
        'ResultWeightBasisText',
        'ResultSampleFractionText',
        'ActivityStartTime/TimeZoneCode',
        'ActivityEndTime/Time',
        'ActivityConductingOrganizationText',
        'MethodDescriptionText',
        'ResultAnalyticalMethod/MethodIdentifier',
        'ResultStatusIdentifier',
        'PreparationStartDate',
        'ResultMeasureValue',
        'ActivityDepthHeightMeasure/MeasureValue',
        'ResultAnalyticalMethod/MethodName',
        'SubjectTaxonomicName',
        'DetectionQuantitationLimitMeasure/MeasureValue',
        'ActivityMediaName',
        'DetectionQuantitationLimitMeasure/MeasureUnitCode',
        'SampleCollectionMethod/MethodIdentifierContext',
        'ProjectIdentifier',
        'HydrologicCondition',
        'LaboratoryName',
        'ResultTimeBasisText',
        'ActivityBottomDepthHeightMeasure/MeasureValue',
        'SampleCollectionEquipmentName'
    }


    # mapping of wqx_semantic_names to their locations in a WQX-0utbound 2.0 Station search result from Water Quality Portal
    station_mappings = {
        'OrganizationIdentifier': '/WQX/Organization/OrganizationDescription/OrganizationIdentifier',
        'OrganizationFormalName': '/WQX/Organization/OrganizationDescription/OrganizationFormalName',
        'MonitoringLocationIdentifier': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/MonitoringLocationIdentifier',
        'MonitoringLocationName': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/MonitoringLocationName',
        'MonitoringLocationTypeName': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/MonitoringLocationTypeName',
        'MonitoringLocationDescriptionText': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/MonitoringLocationDescriptionText',
        'HUCEightDigitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/HUCEightDigitCode',
        'DrainageAreaMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/DrainageAreaMeasure/MeasureValue',
        'DrainageAreaMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/DrainageAreaMeasure/MeasureUnitCode',
        'ContributingDrainageAreaMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/ContributingDrainageAreaMeasure/MeasureValue',
        'ContributingDrainageAreaMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationIdentity/ContributingDrainageAreaMeasure/MeasureUnitCode',
        'LatitudeMeasure': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/LatitudeMeasure',
        'LongitudeMeasure': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/LongitudeMeasure',
        'SourceMapScaleNumeric': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/SourceMapScaleNumeric',
        'HorizontalAccuracyMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/HorizontalAccuracyMeasure/MeasureValue',
        'HorizontalAccuracyMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/HorizontalAccuracyMeasure/MeasureUnitCode',
        'HorizontalCollectionMethodName': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/HorizontalCollectionMethodName',
        'HorizontalCoordinateReferenceSystemDatumName': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/HorizontalCoordinateReferenceSystemDatumName',
        'VerticalMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalMeasure/MeasureValue',
        'VerticalMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalMeasure/MeasureUnitCode',
        'VerticalAccuracyMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalAccuracyMeasure/MeasureValue',
        'VerticalAccuracyMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalAccuracyMeasure/MeasureUnitCode',
        'VerticalCollectionMethodName': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalCollectionMethodName',
        'VerticalCoordinateReferenceSystemDatumName': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/VerticalCoordinateReferenceSystemDatumName',
        'CountryCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/CountryCode',
        'StateCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/StateCode',
        'CountyCode': '/WQX/Organization/MonitoringLocation/MonitoringLocationGeospatial/CountyCode',
        'AquiferName': '/WQX/Organization/MonitoringLocation/WellInformation/AquiferName',
        'FormationTypeText': '/WQX/Organization/MonitoringLocation/WellInformation/FormationTypeText',
        'AquiferTypeName': '/WQX/Organization/MonitoringLocation/WellInformation/AquiferTypeName',
        'ConstructionDateText': '/WQX/Organization/MonitoringLocation/WellInformation/ConstructionDateText',
        'WellDepthMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/WellInformation/WellDepthMeasure/MeasureValue',
        'WellDepthMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/WellInformation/WellDepthMeasure/MeasureUnitCode',
        'WellHoleDepthMeasure/MeasureValue': '/WQX/Organization/MonitoringLocation/WellInformation/WellHoleDepthMeasure/MeasureValue',
        'WellHoleDepthMeasure/MeasureUnitCode': '/WQX/Organization/MonitoringLocation/WellInformation/WellHoleDepthMeasure/MeasureUnitCode'
    }

    # mapping of wqx_semantic_names to their locations in a WQX-0utbound 2.0 Result search result from Water Quality Portal
    result_mappings = {
        'OrganizationIdentifier': '/WQX/Organization/OrganizationDescription/OrganizationIdentifier',
        'OrganizationFormalName': '/WQX/Organization/OrganizationDescription/OrganizationFormalName',
        'ActivityIdentifier': '/WQX/Organization/Activity/ActivityDescription/ActivityIdentifier',
        'ActivityTypeCode': '/WQX/Organization/Activity/ActivityDescription/ActivityTypeCode',
        'ActivityMediaName': '/WQX/Organization/Activity/ActivityDescription/ActivityMediaName',
        'ActivityMediaSubdivisionName': '/WQX/Organization/Activity/ActivityDescription/ActivityMediaSubdivisionName',
        'ActivityStartDate': '/WQX/Organization/Activity/ActivityDescription/ActivityStartDate',
        'ActivityStartTime/Time': '/WQX/Organization/Activity/ActivityDescription/ActivityStartTime/Time',
        'ActivityStartTime/TimeZoneCode': '/WQX/Organization/Activity/ActivityDescription/ActivityStartTime/TimeZoneCode',
        'ActivityEndDate': '/WQX/Organization/Activity/ActivityDescription/ActivityEndDate',
        'ActivityEndTime/Time': '/WQX/Organization/Activity/ActivityDescription/ActivityEndTime/Time',
        'ActivityEndTime/TimeZoneCode': '/WQX/Organization/Activity/ActivityDescription/ActivityEndTime/TimeZoneCode',
        'ActivityDepthHeightMeasure/MeasureValue': '/WQX/Organization/Activity/ActivityDescription/ActivityDepthHeightMeasure/MeasureValue',
        'ActivityDepthHeightMeasure/MeasureUnitCode': '/WQX/Organization/Activity/ActivityDescription/ActivityDepthHeightMeasure/MeasureUnitCode',
        'ActivityDepthAltitudeReferencePointText': '/WQX/Organization/Activity/ActivityDescription/ActivityDepthAltitudeReferencePointText',
        'ActivityTopDepthHeightMeasure/MeasureValue': '/WQX/Organization/Activity/ActivityDescription/ActivityTopDepthHeightMeasure/MeasureValue',
        'ActivityTopDepthHeightMeasure/MeasureUnitCode': '/WQX/Organization/Activity/ActivityDescription/ActivityTopDepthHeightMeasure/MeasureUnitCode',
        'ActivityBottomDepthHeightMeasure/MeasureValue': '/WQX/Organization/Activity/ActivityDescription/ActivityBottomDepthHeightMeasure/MeasureValue',
        'ActivityBottomDepthHeightMeasure/MeasureUnitCode': '/WQX/Organization/Activity/ActivityDescription/ActivityBottomDepthHeightMeasure/MeasureUnitCode',
        'ProjectIdentifier': '/WQX/Organization/Activity/ActivityDescription/ProjectIdentifier',
        'ActivityConductingOrganizationText': '/WQX/Organization/Activity/ActivityDescription/ActivityConductingOrganizationText',
        'MonitoringLocationIdentifier': '/WQX/Organization/Activity/ActivityDescription/MonitoringLocationIdentifier',
        'ActivityCommentText': '/WQX/Organization/Activity/ActivityDescription/ActivityCommentText',
        'SampleAquifer': '/WQX/Organization/Activity/ActivityDescription/SampleAquifer',
        'HydrologicCondition': '/WQX/Organization/Activity/ActivityDescription/HydrologicCondition',
        'HydrologicEvent': '/WQX/Organization/Activity/ActivityDescription/HydrologicEvent',
        'SampleCollectionMethod/MethodIdentifier': '/WQX/Organization/Activity/SampleDescription/SampleCollectionMethod/MethodIdentifier',
        'SampleCollectionMethod/MethodIdentifierContext': '/WQX/Organization/Activity/SampleDescription/SampleCollectionMethod/MethodIdentifierContext',
        'SampleCollectionMethod/MethodName': '/WQX/Organization/Activity/SampleDescription/SampleCollectionMethod/MethodName',
        'SampleCollectionEquipmentName': '/WQX/Organization/Activity/SampleDescription/SampleCollectionEquipmentName',
        'ResultDetectionConditionText': '/WQX/Organization/Activity/Result/ResultDescription/ResultDetectionConditionText',
        'CharacteristicName': '/WQX/Organization/Activity/Result/ResultDescription/CharacteristicName',
        'ResultSampleFractionText': '/WQX/Organization/Activity/Result/ResultDescription/ResultSampleFractionText',
        'ResultMeasureValue': '/WQX/Organization/Activity/Result/ResultDescription/ResultMeasure/ResultMeasureValue',
        'ResultMeasure/MeasureUnitCode': '/WQX/Organization/Activity/Result/ResultDescription/ResultMeasure/MeasureUnitCode',
        'MeasureQualifierCode': '/WQX/Organization/Activity/Result/ResultDescription/ResultMeasure/MeasureQualifierCode',
        'ResultStatusIdentifier': '/WQX/Organization/Activity/Result/ResultDescription/ResultStatusIdentifier',
        'StatisticalBaseCode': '/WQX/Organization/Activity/Result/ResultDescription/StatisticalBaseCode',
        'ResultValueTypeName': '/WQX/Organization/Activity/Result/ResultDescription/ResultValueTypeName',
        'ResultWeightBasisText': '/WQX/Organization/Activity/Result/ResultDescription/ResultWeightBasisText',
        'ResultTimeBasisText': '/WQX/Organization/Activity/Result/ResultDescription/ResultTimeBasisText',
        'ResultTemperatureBasisText': '/WQX/Organization/Activity/Result/ResultDescription/ResultTemperatureBasisText',
        'ResultParticleSizeBasisText': '/WQX/Organization/Activity/Result/ResultDescription/ResultParticleSizeBasisText',
        'PrecisionValue': '/WQX/Organization/Activity/Result/ResultDescription/DataQuality/PrecisionValue',
        'ResultCommentText': '/WQX/Organization/Activity/Result/ResultDescription/ResultCommentText',
        'USGSPCode': '/WQX/Organization/Activity/Result/ResultDescription/USGSPCode',
        'ResultDepthHeightMeasure/MeasureValue': '/WQX/Organization/Activity/Result/ResultDescription/ResultDepthHeightMeasure/MeasureValue',
        'ResultDepthHeightMeasure/MeasureUnitCode': '/WQX/Organization/Activity/Result/ResultDescription/ResultDepthHeightMeasure/MeasureUnitCode',
        'ResultDepthAltitudeReferencePointText': '/WQX/Organization/Activity/Result/ResultDescription/ResultDepthAltitudeReferencePointText',
        'SubjectTaxonomicName': '/WQX/Organization/Activity/Result/BiologicalResultDescription/SubjectTaxonomicName',
        'SampleTissueAnatomyName': '/WQX/Organization/Activity/Result/BiologicalResultDescription/SampleTissueAnatomyName',
        'ResultAnalyticalMethod/MethodIdentifier': '/WQX/Organization/Activity/Result/ResultAnalyticalMethod/MethodIdentifier',
        'ResultAnalyticalMethod/MethodIdentifierContext': '/WQX/Organization/Activity/Result/ResultAnalyticalMethod/MethodIdentifierContext',
        'ResultAnalyticalMethod/MethodName': '/WQX/Organization/Activity/Result/ResultAnalyticalMethod/MethodName',
        'MethodDescriptionText': '/WQX/Organization/Activity/Result/ResultAnalyticalMethod/MethodDescriptionText',
        'LaboratoryName': '/WQX/Organization/Activity/Result/ResultLabInformation/LaboratoryName',
        'AnalysisStartDate': '/WQX/Organization/Activity/Result/ResultLabInformation/AnalysisStartDate',
        'ResultLaboratoryCommentText': '/WQX/Organization/Activity/Result/ResultLabInformation/ResultLaboratoryCommentText',
        'DetectionQuantitationLimitTypeName': '/WQX/Organization/Activity/Result/ResultLabInformation/ResultDetectionQuantitationLimit/DetectionQuantitationLimitTypeName',
        'DetectionQuantitationLimitMeasure/MeasureValue': '/WQX/Organization/Activity/Result/ResultLabInformation/ResultDetectionQuantitationLimit/DetectionQuantitationLimitMeasure/MeasureValue',
        'DetectionQuantitationLimitMeasure/MeasureUnitCode': '/WQX/Organization/Activity/Result/ResultLabInformation/ResultDetectionQuantitationLimit/DetectionQuantitationLimitMeasure/MeasureUnitCode',
        'PreparationStartDate': '/WQX/Organization/Activity/Result/LabSamplePreparation/PreparationStartDate'
    }

    # Message format definitions for mapping WQX XML paths to tabular rows. Every
    # node identified by such a path requires a corresponding row in the tabular form.
    station_row_expr = '/WQX/Organization/MonitoringLocation'
    result_row_expr = '/WQX/Organization/Activity/Result'

    def station_row_nodepath(self):
        return '.' + self.station_row_expr

    def result_row_nodepath(self):
        return '.' + self.result_row_expr


    def empty_station_dataframe(self):
        dataframe = pandas.DataFrame(index=self.station_mappings.keys())
        return dataframe



wqx_semantic_particles = [semantic_name.split('/') for semantic_name in wqx_semantic_names]

particles = set()
for particle_seq in wqx_semantic_particles:
    for particle in particle_seq:
        particles.add(particle)

if True:
    atoms = set()
    import re
    for particle in particles:
        abbr = ''
        for segment in re.findall('[A-Z][a-z]*', particle):
            atoms.add(segment)
            abbr += segment[0].lower()
        print(particle + ' (' + abbr + ')')

semantic_pieces = '\n\n\nsemantic_namepieces = (\n    \'' + '\',\n    \''.join(particles) + '\'\n)'

with open('wqx_mappings.py', 'a') as wqx_mappings_script:
    wqx_mappings_script.write(semantic_pieces)






semantic_namepieces = (
    'ActivityIdentifier',
    'MethodIdentifierContext',
    'MonitoringLocationTypeName',
    'SampleAquifer',
    'CountyCode',
    'PrecisionValue',
    'HorizontalCoordinateReferenceSystemDatumName',
    'Time',
    'SampleTissueAnatomyName',
    'VerticalMeasure',
    'StatisticalBaseCode',
    'ResultWeightBasisText',
    'VerticalCollectionMethodName',
    'MeasureUnitCode',
    'ResultDetectionConditionText',
    'ResultSampleFractionText',
    'MethodDescriptionText',
    'WellDepthMeasure',
    'OrganizationIdentifier',
    'VerticalAccuracyMeasure',
    'TimeZoneCode',
    'ProjectIdentifier',
    'MethodName',
    'ActivityConductingOrganizationText',
    'CountryCode',
    'ResultStatusIdentifier',
    'LaboratoryName',
    'FormationTypeText',
    'AnalysisStartDate',
    'HorizontalAccuracyMeasure',
    'DetectionQuantitationLimitTypeName',
    'ResultLaboratoryCommentText',
    'VerticalCoordinateReferenceSystemDatumName',
    'SampleCollectionMethod',
    'ResultTemperatureBasisText',
    'AquiferTypeName',
    'ResultParticleSizeBasisText',
    'ActivityDepthAltitudeReferencePointText',
    'ResultAnalyticalMethod',
    'USGSPCode',
    'ResultMeasureValue',
    'ActivityTypeCode',
    'DetectionQuantitationLimitMeasure',
    'WellHoleDepthMeasure',
    'CharacteristicName',
    'HydrologicCondition',
    'ResultDepthAltitudeReferencePointText',
    'ActivityTopDepthHeightMeasure',
    'ActivityBottomDepthHeightMeasure',
    'LongitudeMeasure',
    'ContributingDrainageAreaMeasure',
    'AquiferName',
    'ResultCommentText',
    'SubjectTaxonomicName',
    'HydrologicEvent',
    'DrainageAreaMeasure',
    'ActivityStartDate',
    'ActivityMediaName',
    'MonitoringLocationName',
    'ResultValueTypeName',
    'MethodIdentifier',
    'MeasureValue',
    'ResultMeasure',
    'MonitoringLocationIdentifier',
    'ActivityDepthHeightMeasure',
    'HorizontalCollectionMethodName',
    'ResultDepthHeightMeasure',
    'HUCEightDigitCode',
    'OrganizationFormalName',
    'MonitoringLocationDescriptionText',
    'ActivityCommentText',
    'LatitudeMeasure',
    'PreparationStartDate',
    'ActivityEndDate',
    'ActivityEndTime',
    'SourceMapScaleNumeric',
    'ConstructionDateText',
    'ActivityStartTime',
    'ResultTimeBasisText',
    'MeasureQualifierCode',
    'ActivityMediaSubdivisionName',
    'SampleCollectionEquipmentName',
    'StateCode'
)
