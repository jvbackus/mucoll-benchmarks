#!/usr/bin/env python

from Gaudi.Configuration import *

from Configurables import LcioEvent, EventDataSvc, MarlinProcessorWrapper, ApplicationMgr
from k4MarlinWrapper.parseConstants import *
from Gaudi.Main import gaudimain
import os

algList = []
evtsvc = EventDataSvc()

CONSTANTS = {}

parseConstants(CONSTANTS)

read = LcioEvent()
read.OutputLevel = INFO
read.Files = [ "output_sim.slcio" ]
algList.append(read)

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = INFO
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Overlay": ["False"],
                     "OverlayChoices": ["False", "Test", "BIB", "Trimmed"],
                     "VertexUnconstrained": ["OFF"],
                     "VertexUnconstrainedChoices": ["ON", "OFF"]
                     }
algList.append(Config)

EventNumber = MarlinProcessorWrapper("EventNumber")
EventNumber.OutputLevel = INFO
EventNumber.ProcessorType = "Statusmonitor"
EventNumber.Parameters = {
                          "HowOften": ["1"]
                          }
algList.append(EventNumber)

MyAIDAProcessor = MarlinProcessorWrapper("MyAIDAProcessor")
MyAIDAProcessor.OutputLevel = INFO
MyAIDAProcessor.ProcessorType = "AIDAProcessor"
MyAIDAProcessor.Parameters = {
                              "Compress": ["1"],
                              "FileName": ["lctuple"],
                              "FileType": ["root"]
                              }
algList.append(MyAIDAProcessor)

InitDD4hep = MarlinProcessorWrapper("InitDD4hep")
InitDD4hep.OutputLevel = INFO
InitDD4hep.ProcessorType = "InitializeDD4hep"
InitDD4hep.Parameters = {
                         "DD4hepXMLFile": [ os.environ.get('MUCOLL_GEO') ],
                         "EncodingStringParameterName": ["GlobalTrackerReadoutID"]
                         }
algList.append(InitDD4hep)

OverlayFalse = MarlinProcessorWrapper("OverlayFalse")
OverlayFalse.OutputLevel = INFO
OverlayFalse.ProcessorType = "OverlayTimingGeneric"
OverlayFalse.Parameters = {
                           "BackgroundFileNames": ["/dev/null"],
                           "Collection_IntegrationTimes": [
                                "VertexBarrelCollection", "-0.18", "0.24",
                                "VertexEndcapCollection", "-0.18", "0.24",
                                "InnerTrackerBarrelCollection", "-0.36", "0.48",
                                "InnerTrackerEndcapCollection", "-0.36", "0.48",
                                "OuterTrackerBarrelCollection", "-0.36", "0.48",
                                "OuterTrackerEndcapCollection", "-0.36", "0.48",
                                "ECalBarrelCollection", "0.25",
                                "ECalEndcapCollection", "0.25",
                                "ECalPlugCollection", "0.25",
                                "HCalBarrelCollection", "0.25",
                                "HCalEndcapCollection", "0.25",
                                "HCalRingCollection", "0.25",
                                "YokeBarrelCollection", "0.25",
                                "YokeEndcapCollection", "0.25"
                           ],
                           "Delta_t": ["1"],
                           "MCParticleCollectionName": ["MCParticle"],
                           "MCPhysicsParticleCollectionName": ["MCPhysicsParticles"],
                           "MergeMCParticles": ["false"],
                           "NBunchtrain": ["0"],
                           "NumberBackground": ["0."],
                           "PhysicsBX": ["1"],
                           "Poisson_random_NOverlay": ["false"],
                           "RandomBx": ["false"],
                           "TPCDriftvelocity": ["0.05"]
                           }
algList.append(OverlayFalse)

VXDBarrelDigitiser = MarlinProcessorWrapper("VXDBarrelDigitiser")
VXDBarrelDigitiser.OutputLevel = INFO
VXDBarrelDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDBarrelDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexBarrelCollection"],
                                 "SimTrkHitRelCollection": ["VXDTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }
algList.append(VXDBarrelDigitiser)

VXDEndcapDigitiser = MarlinProcessorWrapper("VXDEndcapDigitiser")
VXDEndcapDigitiser.OutputLevel = INFO
VXDEndcapDigitiser.ProcessorType = "DDPlanarDigiProcessor"
VXDEndcapDigitiser.Parameters = {
                                 "CorrectTimesForPropagation": ["true"],
                                 "IsStrip": ["false"],
                                 "ResolutionT": ["0.03"],
                                 "ResolutionU": ["0.005"],
                                 "ResolutionV": ["0.005"],
                                 "SimTrackHitCollectionName": ["VertexEndcapCollection"],
                                 "SimTrkHitRelCollection": ["VXDEndcapTrackerHitRelations"],
                                 "SubDetectorName": ["Vertex"],
                                 "TimeWindowMax": ["0.15"],
                                 "TimeWindowMin": ["-0.09"],
                                 "TrackerHitCollectionName": ["VXDEndcapTrackerHits"],
                                 "UseTimeWindow": ["true"]
                                 }
algList.append(VXDEndcapDigitiser)

InnerPlanarDigiProcessor = MarlinProcessorWrapper("InnerPlanarDigiProcessor")
InnerPlanarDigiProcessor.OutputLevel = INFO
InnerPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["InnerTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["ITBarrelHitsRelations"],
                                       "SubDetectorName": ["InnerTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["ITrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }
algList.append(InnerPlanarDigiProcessor)

InnerEndcapPlanarDigiProcessor = MarlinProcessorWrapper("InnerEndcapPlanarDigiProcessor")
InnerEndcapPlanarDigiProcessor.OutputLevel = INFO
InnerEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
InnerEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["InnerTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["ITEndcapHitsRelations"],
                                             "SubDetectorName": ["InnerTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["ITrackerEndcapHits"],
                                             "UseTimeWindow": ["true"]
                                             }
algList.append(InnerEndcapPlanarDigiProcessor)

OuterPlanarDigiProcessor = MarlinProcessorWrapper("OuterPlanarDigiProcessor")
OuterPlanarDigiProcessor.OutputLevel = INFO
OuterPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterPlanarDigiProcessor.Parameters = {
                                       "CorrectTimesForPropagation": ["true"],
                                       "IsStrip": ["false"],
                                       "ResolutionT": ["0.06"],
                                       "ResolutionU": ["0.007"],
                                       "ResolutionV": ["0.090"],
                                       "SimTrackHitCollectionName": ["OuterTrackerBarrelCollection"],
                                       "SimTrkHitRelCollection": ["OTBarrelHitsRelations"],
                                       "SubDetectorName": ["OuterTrackers"],
                                       "TimeWindowMax": ["0.3"],
                                       "TimeWindowMin": ["-0.18"],
                                       "TrackerHitCollectionName": ["OTrackerHits"],
                                       "UseTimeWindow": ["true"]
                                       }
algList.append(OuterPlanarDigiProcessor)

OuterEndcapPlanarDigiProcessor = MarlinProcessorWrapper("OuterEndcapPlanarDigiProcessor")
OuterEndcapPlanarDigiProcessor.OutputLevel = INFO
OuterEndcapPlanarDigiProcessor.ProcessorType = "DDPlanarDigiProcessor"
OuterEndcapPlanarDigiProcessor.Parameters = {
                                             "CorrectTimesForPropagation": ["true"],
                                             "IsStrip": ["false"],
                                             "ResolutionT": ["0.06"],
                                             "ResolutionU": ["0.007"],
                                             "ResolutionV": ["0.090"],
                                             "SimTrackHitCollectionName": ["OuterTrackerEndcapCollection"],
                                             "SimTrkHitRelCollection": ["OTEndcapHitsRelations"],
                                             "SubDetectorName": ["OuterTrackers"],
                                             "TimeWindowMax": ["0.3"],
                                             "TimeWindowMin": ["-0.18"],
                                             "TrackerHitCollectionName": ["OTrackerEndcapHits"],
                                             "UseTimeWindow": ["true"]
                                             }
algList.append(OuterEndcapPlanarDigiProcessor)

MyDDCaloDigi = MarlinProcessorWrapper("MyDDCaloDigi")
MyDDCaloDigi.OutputLevel = INFO
MyDDCaloDigi.ProcessorType = "DDCaloDigi"
MyDDCaloDigi.Parameters = {
                           "CalibECALMIP": ["0.0001"],
                           "CalibHCALMIP": ["0.0001"],
                           "CalibrECAL": ["35.8411424188", "35.8411424188"],
                           "CalibrHCALBarrel": ["49.2031079063"],
                           "CalibrHCALEndcap": ["53.6263377733"],
                           "CalibrHCALOther": ["62.2125698179"],
                           "ECALBarrelTimeWindowMax": ["10"],
                           "ECALCollections": ["ECalBarrelCollection", "ECalEndcapCollection", "ECalPlugCollection"],
                           "ECALCorrectTimesForPropagation": ["1"],
                           "ECALDeltaTimeHitResolution": ["10"],
                           "ECALEndcapCorrectionFactor": ["1.0672142727"],
                           "ECALEndcapTimeWindowMax": ["10"],
                           "ECALGapCorrection": ["1"],
                           "ECALGapCorrectionFactor": ["1"],
                           "ECALLayers": ["41", "100"],
                           "ECALModuleGapCorrectionFactor": ["0.0"],
                           "ECALOutputCollection0": ["ECALBarrel"],
                           "ECALOutputCollection1": ["ECALEndcap"],
                           "ECALOutputCollection2": ["ECALOther"],
                           "ECALSimpleTimingCut": ["true"],
                           "ECALThreshold": ["0.002"],
                           "ECALThresholdUnit": ["GeV"],
                           "ECALTimeResolution": ["10"],
                           "ECALTimeWindowMin": ["-1"],
                           "ECAL_PPD_N_Pixels": ["10000"],
                           "ECAL_PPD_N_Pixels_uncertainty": ["0.05"],
                           "ECAL_PPD_PE_per_MIP": ["7"],
                           "ECAL_apply_realistic_digi": ["0"],
                           "ECAL_deadCellRate": ["0"],
                           "ECAL_deadCell_memorise": ["false"],
                           "ECAL_default_layerConfig": ["000000000000000"],
                           "ECAL_elec_noise_mips": ["0"],
                           "ECAL_maxDynamicRange_MIP": ["2500"],
                           "ECAL_miscalibration_correl": ["0"],
                           "ECAL_miscalibration_uncorrel": ["0"],
                           "ECAL_miscalibration_uncorrel_memorise": ["false"],
                           "ECAL_pixel_spread": ["0.05"],
                           "ECAL_strip_absorbtionLength": ["1e+06"],
                           "HCALBarrelTimeWindowMax": ["10"],
                           "HCALCollections": [
                                "HCalBarrelCollection",
                                "HCalEndcapCollection",
                                "HCalRingCollection"
                           ],
                           "HCALCorrectTimesForPropagation": ["1"],
                           "HCALDeltaTimeHitResolution": ["10"],
                           "HCALEndcapCorrectionFactor": ["1.000"],
                           "HCALEndcapTimeWindowMax": ["10"],
                           "HCALGapCorrection": ["1"],
                           "HCALLayers": ["100"],
                           "HCALModuleGapCorrectionFactor": ["0.5"],
                           "HCALOutputCollection0": ["HCALBarrel"],
                           "HCALOutputCollection1": ["HCALEndcap"],
                           "HCALOutputCollection2": ["HCALOther"],
                           "HCALSimpleTimingCut": ["true"],
                           "HCALThreshold": ["0.002"],
                           "HCALThresholdUnit": ["GeV"],
                           "HCALTimeResolution": ["10"],
                           "HCALTimeWindowMin": ["-1"],
                           "HCAL_PPD_N_Pixels": ["400"],
                           "HCAL_PPD_N_Pixels_uncertainty": ["0.05"],
                           "HCAL_PPD_PE_per_MIP": ["10"],
                           "HCAL_apply_realistic_digi": ["0"],
                           "HCAL_deadCellRate": ["0"],
                           "HCAL_deadCell_memorise": ["false"],
                           "HCAL_elec_noise_mips": ["0"],
                           "HCAL_maxDynamicRange_MIP": ["200"],
                           "HCAL_miscalibration_correl": ["0"],
                           "HCAL_miscalibration_uncorrel": ["0"],
                           "HCAL_miscalibration_uncorrel_memorise": ["false"],
                           "HCAL_pixel_spread": ["0"],
                           "Histograms": ["0"],
                           "IfDigitalEcal": ["0"],
                           "IfDigitalHcal": ["0"],
                           "MapsEcalCorrection": ["0"],
                           "RelationOutputCollection": ["RelationCaloHit"],
                           "RootFile": ["Digi_SiW.root"],
                           "StripEcal_default_nVirtualCells": ["9"],
                           "UseEcalTiming": ["1"],
                           "UseHcalTiming": ["1"],
                           "energyPerEHpair": ["3.6"]
                           }
algList.append(MyDDCaloDigi)

MyDDSimpleMuonDigi = MarlinProcessorWrapper("MyDDSimpleMuonDigi")
MyDDSimpleMuonDigi.OutputLevel = INFO
MyDDSimpleMuonDigi.ProcessorType = "DDSimpleMuonDigi"
MyDDSimpleMuonDigi.Parameters = {
                                 "CalibrMUON": ["70.1"],
                                 "MUONCollections": ["YokeBarrelCollection", "YokeEndcapCollection"],
                                 "MUONOutputCollection": ["MUON"],
                                 "MaxHitEnergyMUON": ["2.0"],
                                 "MuonThreshold": ["1e-06"],
                                 "RelationOutputCollection": ["RelationMuonHit"]
                                 }
algList.append(MyDDSimpleMuonDigi)

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
                         "DropCollectionNames": ["SeedTracks"],
                         "DropCollectionTypes": [],
                         "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
                         "KeepCollectionNames": [],
                         "LCIOOutputFile": ["output_digi.slcio"],
                         "LCIOWriteMode": ["WRITE_NEW"]
                         }
algList.append(Output_REC)

ApplicationMgr( TopAlg = algList,
                EvtSel = 'NONE',
                EvtMax   = 10,
                ExtSvc = [evtsvc],
                OutputLevel=INFO
              )

gmain = gaudimain()
gmain.run(False)

