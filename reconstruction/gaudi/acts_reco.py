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
read.Files = ["output_digi.slcio"]
algList.append(read)

Config = MarlinProcessorWrapper("Config")
Config.OutputLevel = INFO
Config.ProcessorType = "CLICRecoConfig"
Config.Parameters = {
                     "Tracking": ["ACTs"],
                     "TrackingChoices": ["Truth", "Conformal", "ACTs"],
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

MyCKFTracking = MarlinProcessorWrapper("MyCKFTracking")
MyCKFTracking.OutputLevel = INFO 
MyCKFTracking.ProcessorType = "ACTSSeededCKFTrackingProc" 
MyCKFTracking.Parameters = {
                            "CKF_Chi2CutOff": ["10"],
                            "CKF_NumMeasurementsCutOff": ["1"],
                            "MatFile": [ os.environ.get('ACTS_MatFile') ],
                            "RunCKF": ["True"],
                            "SeedFinding_CollisionRegion": ["1"],
                            "SeedFinding_DeltaRMax": ["80"],
                            "SeedFinding_DeltaRMin": ["5"],
                            "SeedFinding_MinPt": ["500"],
                            "SeedFinding_RMax": ["150"],
                            "SeedFinding_RadLengthPerSeed": ["0.1"],
                            "SeedFinding_SigmaScattering": ["50"],
                            "SeedingLayers": [
                                "13", "2", "13", "6", 
                                "13", "10", "13", "14", 
                                "14", "2", "14", "6", 
                                "14", "10", "14", "14",
                                "15", "2", "15", "6",
                                "15", "10", "15", "14"
                            ],
                            "TGeoFile": [ os.environ.get('ACTS_TGeoFile') ],
                            "TrackCollectionName": ["SiTracksACTs"],
                            "TrackerHitCollectionNames": [
                                "VXDTrackerHits",
                                "VXDEndcapTrackerHits",
                                "ITrackerHits",
                                "ITrackerEndcapHits",
                                "OTrackerHits",
                                "OTrackerEndcapHits"
                            ]
                            }
algList.append(MyCKFTracking)

MyTrackDeduper = MarlinProcessorWrapper("MyTrackDeduper")
MyTrackDeduper.OutputLevel = INFO 
MyTrackDeduper.ProcessorType = "ACTSDuplicateRemoval" 
MyTrackDeduper.Parameters = {
                             "InputTrackCollectionName": ["SiTracksACTs"],
                             "OutputTrackCollectionName": ["SiTracks"]
                             }
algList.append(MyTrackDeduper)

Refit = MarlinProcessorWrapper("Refit")
Refit.OutputLevel = INFO
Refit.ProcessorType = "RefitFinal"
Refit.Parameters = {
                    "EnergyLossOn": ["true"],
                    "InputRelationCollectionName": ["MCParticle_Tracks"],
                    "InputTrackCollectionName": ["SiTracks"],
                    "Max_Chi2_Incr": ["1.79769e+30"],
                    "MinClustersOnTrackAfterFit": ["3"],
                    "MultipleScatteringOn": ["true"],
                    "NHitsCuts": ["1,2", "4", "3,4", "3"],
                    "OutputRelationCollectionName": ["SiTracks_Refitted_Relation"],
                    "OutputTrackCollectionName": ["SiTracks_Refitted"],
                    "ReducedChi2Cut": ["-1"],
                    "ReferencePoint": ["-1"],
                    "SmoothOn": ["false"],
                    "extrapolateForward": ["true"]
                    }
algList.append(Refit)

MyDDMarlinPandora = MarlinProcessorWrapper("MyDDMarlinPandora")
MyDDMarlinPandora.OutputLevel = INFO
MyDDMarlinPandora.ProcessorType = "DDPandoraPFANewProcessor"
MyDDMarlinPandora.Parameters = {
                                "ClusterCollectionName": ["PandoraClusters"],
                                "CreateGaps": ["false"],
                                "CurvatureToMomentumFactor": ["0.00015"],
                                "D0TrackCut": ["200"],
                                "D0UnmatchedVertexTrackCut": ["5"],
                                "DigitalMuonHits": ["0"],
                                "ECalBarrelNormalVector": ["0", "0", "1"],
                                "ECalCaloHitCollections": ["ECALBarrel", "ECALEndcap", "ECALOther"],
                                "ECalMipThreshold": ["0.5"],
                                "ECalScMipThreshold": ["0"],
                                "ECalScToEMGeVCalibration": ["1"],
                                "ECalScToHadGeVCalibrationBarrel": ["1"],
                                "ECalScToHadGeVCalibrationEndCap": ["1"],
                                "ECalScToMipCalibration": ["1"],
                                "ECalSiMipThreshold": ["0"],
                                "ECalSiToEMGeVCalibration": ["1"],
                                "ECalSiToHadGeVCalibrationBarrel": ["1"],
                                "ECalSiToHadGeVCalibrationEndCap": ["1"],
                                "ECalSiToMipCalibration": ["1"],
                                "ECalToEMGeVCalibration": ["1.02373335516"],
                                "ECalToHadGeVCalibrationBarrel": ["1.24223718397"],
                                "ECalToHadGeVCalibrationEndCap": ["1.24223718397"],
                                "ECalToMipCalibration": ["181.818"],
                                "EMConstantTerm": ["0.01"],
                                "EMStochasticTerm": ["0.17"],
                                "FinalEnergyDensityBin": ["110."],
                                "HCalBarrelNormalVector": ["0", "0", "1"],
                                "HCalCaloHitCollections": ["HCALBarrel", "HCALEndcap", "HCALOther"],
                                "HCalMipThreshold": ["0.3"],
                                "HCalToEMGeVCalibration": ["1.02373335516"],
                                "HCalToHadGeVCalibration": ["1.01799349172"],
                                "HCalToMipCalibration": ["40.8163"],
                                "HadConstantTerm": ["0.03"],
                                "HadStochasticTerm": ["0.6"],
                                "InputEnergyCorrectionPoints": [],
                                "KinkVertexCollections": ["KinkVertices"],
                                "LayersFromEdgeMaxRearDistance": ["250"],
                                "MCParticleCollections": ["MCParticle"],
                                "MaxBarrelTrackerInnerRDistance": ["200"],
                                "MaxClusterEnergyToApplySoftComp": ["2000."],
                                "MaxHCalHitHadronicEnergy": ["1000000"],
                                "MaxTrackHits": ["5000"],
                                "MaxTrackSigmaPOverP": ["0.15"],
                                "MinBarrelTrackerHitFractionOfExpected": ["0"],
                                "MinCleanCorrectedHitEnergy": ["0.1"],
                                "MinCleanHitEnergy": ["0.5"],
                                "MinCleanHitEnergyFraction": ["0.01"],
                                "MinFtdHitsForBarrelTrackerHitFraction": ["0"],
                                "MinFtdTrackHits": ["0"],
                                "MinMomentumForTrackHitChecks": ["0"],
                                "MinTpcHitFractionOfExpected": ["0"],
                                "MinTrackECalDistanceFromIp": ["0"],
                                "MinTrackHits": ["0"],
                                "MuonBarrelBField": ["-1.34"],
                                "MuonCaloHitCollections": ["MUON"],
                                "MuonEndCapBField": ["0.01"],
                                "MuonHitEnergy": ["0.5"],
                                "MuonToMipCalibration": ["19607.8"],
                                "NEventsToSkip": ["0"],
                                "NOuterSamplingLayers": ["3"],
                                "OutputEnergyCorrectionPoints": [],
                                "PFOCollectionName": ["PandoraPFOs"],
                                "PandoraSettingsXmlFile": ["PandoraSettings/PandoraSettingsDefault.xml"],
                                "ProngVertexCollections": ["ProngVertices"],
                                "ReachesECalBarrelTrackerOuterDistance": ["-100"],
                                "ReachesECalBarrelTrackerZMaxDistance": ["-50"],
                                "ReachesECalFtdZMaxDistance": ["1"],
                                "ReachesECalMinFtdLayer": ["0"],
                                "ReachesECalNBarrelTrackerHits": ["0"],
                                "ReachesECalNFtdHits": ["0"],
                                "RelCaloHitCollections": ["RelationCaloHit", "RelationMuonHit"],
                                "RelTrackCollections": ["SiTracks_Refitted_Relation"],
                                "ShouldFormTrackRelationships": ["1"],
                                "SoftwareCompensationEnergyDensityBins": [
                                    "0", "2.", "5.", "7.5", "9.5",
                                    "13.", "16.", "20.", "23.5", "28.",
                                    "33.", "40.", "50.", "75.", "100."
                                ],
                                "SoftwareCompensationWeights": [
                                    "1.61741", "-0.00444385", "2.29683e-05",
                                    "-0.0731236", "-0.00157099", "-7.09546e-07",
                                    "0.868443", "1.0561", "-0.0238574"
                                ],
                                "SplitVertexCollections": ["SplitVertices"],
                                "StartVertexAlgorithmName": ["PandoraPFANew"],
                                "StartVertexCollectionName": ["PandoraStartVertices"],
                                "StripSplittingOn": ["0"],
                                "TrackCollections": ["SiTracks_Refitted"],
                                "TrackCreatorName": ["DDTrackCreatorCLIC"],
                                "TrackStateTolerance": ["0"],
                                "TrackSystemName": ["DDKalTest"],
                                "UnmatchedVertexTrackMaxEnergy": ["5"],
                                "UseEcalScLayers": ["0"],
                                "UseNonVertexTracks": ["1"],
                                "UseOldTrackStateCalculation": ["0"],
                                "UseUnmatchedNonVertexTracks": ["0"],
                                "UseUnmatchedVertexTracks": ["1"],
                                "V0VertexCollections": ["V0Vertices"],
                                "YokeBarrelNormalVector": ["0", "0", "1"],
                                "Z0TrackCut": ["200"],
                                "Z0UnmatchedVertexTrackCut": ["5"],
                                "ZCutForNonVertexTracks": ["250"]
                                }
algList.append(MyDDMarlinPandora)

MyRecoMCTruthLinker = MarlinProcessorWrapper("MyRecoMCTruthLinker")
MyRecoMCTruthLinker.OutputLevel = INFO
MyRecoMCTruthLinker.ProcessorType = "RecoMCTruthLinker"
MyRecoMCTruthLinker.Parameters = {
                                  "BremsstrahlungEnergyCut": ["1"],
                                  "CalohitMCTruthLinkName": ["CalohitMCTruthLink"],
                                  "ClusterCollection": ["PandoraClusters"],
                                  "ClusterMCTruthLinkName": ["ClusterMCTruthLink"],
                                  "FullRecoRelation": ["false"],
                                  "InvertedNonDestructiveInteractionLogic": ["false"],
                                  "KeepDaughtersPDG": ["22", "111", "310", "13", "211", "321", "3120"],
                                  "MCParticleCollection": ["MCParticle"],
                                  "MCParticlesSkimmedName": ["MCParticlesSkimmed"],
                                  "MCTruthClusterLinkName": [],
                                  "MCTruthRecoLinkName": [],
                                  "MCTruthTrackLinkName": [],
                                  "RecoMCTruthLinkName": ["RecoMCTruthLink"],
                                  "RecoParticleCollection": ["PandoraPFOs"],
                                  "SaveBremsstrahlungPhotons": ["false"],
                                  "SimCaloHitCollections": [
                                    "ECalBarrelCollection",
                                    "ECalEndcapCollection",
                                    "HCalBarrelCollection",
                                    "HCalEndcapCollection",
                                    "HCalRingCollection",
                                    "YokeBarrelCollection",
                                    "YokeEndcapCollection"
                                  ],
                                  "SimCalorimeterHitRelationNames": ["RelationCaloHit", "RelationMuonHit"],
                                  "SimTrackerHitCollections": [
                                    "VertexBarrelCollection",
                                    "VertexEndcapCollection",
                                    "InnerTrackerBarrelCollection",
                                    "InnerTrackerEndcapCollection",
                                    "OuterTrackerBarrelCollection",
                                    "OuterTrackerEndcapCollection"
                                  ],
                                  "TrackCollection": ["SiTracks_Refitted"],
                                  "TrackMCTruthLinkName": ["SiTracksMCTruthLink"],
                                  "TrackerHitsRelInputCollections": [
                                    "VXDTrackerHitRelations",
                                    "VXDEndcapTrackerHitRelations",
                                    "ITBarrelHitsRelations",
                                    "ITEndcapHitsRelations",
                                    "OTBarrelHitsRelations",
                                    "OTEndcapHitsRelations"
                                  ],
                                  "UseTrackerHitRelations": ["true"],
                                  "UsingParticleGun": ["false"],
                                  "daughtersECutMeV": ["10"]
                                  }
algList.append(MyRecoMCTruthLinker)

MyTrackChecker = MarlinProcessorWrapper("MyTrackChecker")
MyTrackChecker.OutputLevel = INFO
MyTrackChecker.ProcessorType = "TrackChecker"
MyTrackChecker.Parameters = {
                             "MCParticleCollectionName": ["MCParticle"],
                             "TrackCollectionName": ["SiTracks_Refitted"],
                             "TrackRelationCollectionName": ["SiTracksMCTruthLink"],
                             "TreeName": ["checktree"],
                             "UseOnlyTree": ["true"]
                             }
algList.append(MyTrackChecker)

CLICPfoSelectorDefault_HE = MarlinProcessorWrapper("CLICPfoSelectorDefault_HE")
CLICPfoSelectorDefault_HE.OutputLevel = INFO
CLICPfoSelectorDefault_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorDefault_HE.Parameters = {
                                        "ChargedPfoLooseTimingCut": ["3"],
                                        "ChargedPfoNegativeLooseTimingCut": ["-1"],
                                        "ChargedPfoNegativeTightTimingCut": ["-0.5"],
                                        "ChargedPfoPtCut": ["0"],
                                        "ChargedPfoPtCutForLooseTiming": ["4"],
                                        "ChargedPfoTightTimingCut": ["1.5"],
                                        "CheckKaonCorrection": ["0"],
                                        "CheckProtonCorrection": ["0"],
                                        "ClusterLessPfoTrackTimeCut": ["10"],
                                        "CorrectHitTimesForTimeOfFlight": ["0"],
                                        "DisplayRejectedPfos": ["1"],
                                        "DisplaySelectedPfos": ["1"],
                                        "FarForwardCosTheta": ["0.975"],
                                        "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                        "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                        "HCalBarrelLooseTimingCut": ["20"],
                                        "HCalBarrelTightTimingCut": ["10"],
                                        "HCalEndCapTimingFactor": ["1"],
                                        "InputPfoCollection": ["PandoraPFOs"],
                                        "KeepKShorts": ["1"],
                                        "MaxMomentumForClusterLessPfos": ["2"],
                                        "MinECalHitsForTiming": ["5"],
                                        "MinHCalEndCapHitsForTiming": ["5"],
                                        "MinMomentumForClusterLessPfos": ["0.5"],
                                        "MinPtForClusterLessPfos": ["0.5"],
                                        "MinimumEnergyForNeutronTiming": ["1"],
                                        "Monitoring": ["0"],
                                        "MonitoringPfoEnergyToDisplay": ["1"],
                                        "NeutralFarForwardLooseTimingCut": ["2"],
                                        "NeutralFarForwardTightTimingCut": ["1"],
                                        "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                        "NeutralHadronLooseTimingCut": ["2.5"],
                                        "NeutralHadronPtCut": ["0"],
                                        "NeutralHadronPtCutForLooseTiming": ["8"],
                                        "NeutralHadronTightTimingCut": ["1.5"],
                                        "PhotonFarForwardLooseTimingCut": ["2"],
                                        "PhotonFarForwardTightTimingCut": ["1"],
                                        "PhotonLooseTimingCut": ["2"],
                                        "PhotonPtCut": ["0"],
                                        "PhotonPtCutForLooseTiming": ["4"],
                                        "PhotonTightTimingCut": ["1"],
                                        "PtCutForTightTiming": ["0.75"],
                                        "SelectedPfoCollection": ["SelectedPandoraPFOs"],
                                        "UseClusterLessPfos": ["1"],
                                        "UseNeutronTiming": ["0"]
                                        }
algList.append(CLICPfoSelectorDefault_HE)

CLICPfoSelectorLoose_HE = MarlinProcessorWrapper("CLICPfoSelectorLoose_HE")
CLICPfoSelectorLoose_HE.OutputLevel = INFO
CLICPfoSelectorLoose_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorLoose_HE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["3"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-2.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-2.0"],
                                      "ChargedPfoPtCut": ["0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4"],
                                      "ChargedPfoTightTimingCut": ["1.5"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["1000."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["20"],
                                      "HCalBarrelTightTimingCut": ["10"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["2"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.25"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["2.5"],
                                      "NeutralFarForwardTightTimingCut": ["1.5"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["2.5"],
                                      "NeutralHadronPtCut": ["0"],
                                      "NeutralHadronPtCutForLooseTiming": ["8"],
                                      "NeutralHadronTightTimingCut": ["1.5"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["2."],
                                      "PhotonPtCut": ["0"],
                                      "PhotonPtCutForLooseTiming": ["4"],
                                      "PhotonTightTimingCut": ["2."],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LooseSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorLoose_HE)

CLICPfoSelectorTight_HE = MarlinProcessorWrapper("CLICPfoSelectorTight_HE")
CLICPfoSelectorTight_HE.OutputLevel = INFO
CLICPfoSelectorTight_HE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorTight_HE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["2.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-0.5"],
                                      "ChargedPfoNegativeTightTimingCut": ["-0.25"],
                                      "ChargedPfoPtCut": ["0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4"],
                                      "ChargedPfoTightTimingCut": ["1.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["10"],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.95"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["20"],
                                      "HCalBarrelTightTimingCut": ["10"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["1.5"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.5"],
                                      "MinPtForClusterLessPfos": ["1.0"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["1.5"],
                                      "NeutralFarForwardTightTimingCut": ["1"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["2.5"],
                                      "NeutralHadronPtCut": ["0.5"],
                                      "NeutralHadronPtCutForLooseTiming": ["8"],
                                      "NeutralHadronTightTimingCut": ["1.5"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["2"],
                                      "PhotonPtCut": ["0.2"],
                                      "PhotonPtCutForLooseTiming": ["4"],
                                      "PhotonTightTimingCut": ["1"],
                                      "PtCutForTightTiming": ["1.0"],
                                      "SelectedPfoCollection": ["TightSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["0"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorTight_HE)

CLICPfoSelectorDefault_LE = MarlinProcessorWrapper("CLICPfoSelectorDefault_LE")
CLICPfoSelectorDefault_LE.OutputLevel = INFO
CLICPfoSelectorDefault_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorDefault_LE.Parameters = {
                                        "ChargedPfoLooseTimingCut": ["10.0"],
                                        "ChargedPfoNegativeLooseTimingCut": ["-5.0"],
                                        "ChargedPfoNegativeTightTimingCut": ["-2.0"],
                                        "ChargedPfoPtCut": ["0.0"],
                                        "ChargedPfoPtCutForLooseTiming": ["4.0"],
                                        "ChargedPfoTightTimingCut": ["3.0"],
                                        "CheckKaonCorrection": ["0"],
                                        "CheckProtonCorrection": ["0"],
                                        "ClusterLessPfoTrackTimeCut": ["10."],
                                        "CorrectHitTimesForTimeOfFlight": ["0"],
                                        "DisplayRejectedPfos": ["1"],
                                        "DisplaySelectedPfos": ["1"],
                                        "FarForwardCosTheta": ["0.975"],
                                        "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                        "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                        "HCalBarrelLooseTimingCut": ["5"],
                                        "HCalBarrelTightTimingCut": ["2.5"],
                                        "HCalEndCapTimingFactor": ["1"],
                                        "InputPfoCollection": ["PandoraPFOs"],
                                        "KeepKShorts": ["1"],
                                        "MaxMomentumForClusterLessPfos": ["5.0"],
                                        "MinECalHitsForTiming": ["5"],
                                        "MinHCalEndCapHitsForTiming": ["5"],
                                        "MinMomentumForClusterLessPfos": ["0.0"],
                                        "MinPtForClusterLessPfos": ["0.0"],
                                        "MinimumEnergyForNeutronTiming": ["1"],
                                        "Monitoring": ["0"],
                                        "MonitoringPfoEnergyToDisplay": ["1"],
                                        "NeutralFarForwardLooseTimingCut": ["4.0"],
                                        "NeutralFarForwardTightTimingCut": ["2.0"],
                                        "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                        "NeutralHadronLooseTimingCut": ["5.0"],
                                        "NeutralHadronPtCut": ["0.0"],
                                        "NeutralHadronPtCutForLooseTiming": ["2.0"],
                                        "NeutralHadronTightTimingCut": ["2.5"],
                                        "PhotonFarForwardLooseTimingCut": ["2"],
                                        "PhotonFarForwardTightTimingCut": ["1"],
                                        "PhotonLooseTimingCut": ["5.0"],
                                        "PhotonPtCut": ["0.0"],
                                        "PhotonPtCutForLooseTiming": ["2.0"],
                                        "PhotonTightTimingCut": ["1.0"],
                                        "PtCutForTightTiming": ["0.75"],
                                        "SelectedPfoCollection": ["LE_SelectedPandoraPFOs"],
                                        "UseClusterLessPfos": ["1"],
                                        "UseNeutronTiming": ["0"]
                                        }
algList.append(CLICPfoSelectorDefault_LE)

CLICPfoSelectorLoose_LE = MarlinProcessorWrapper("CLICPfoSelectorLoose_LE")
CLICPfoSelectorLoose_LE.OutputLevel = INFO
CLICPfoSelectorLoose_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorLoose_LE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["10.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-20.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-20.0"],
                                      "ChargedPfoPtCut": ["0.0"],
                                      "ChargedPfoPtCutForLooseTiming": ["4.0"],
                                      "ChargedPfoTightTimingCut": ["5.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["50."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["10"],
                                      "HCalBarrelTightTimingCut": ["5"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["5.0"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.0"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["10.0"],
                                      "NeutralFarForwardTightTimingCut": ["5.0"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["10.0"],
                                      "NeutralHadronPtCut": ["0.0"],
                                      "NeutralHadronPtCutForLooseTiming": ["2.0"],
                                      "NeutralHadronTightTimingCut": ["5.0"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["10.0"],
                                      "PhotonPtCut": ["0.0"],
                                      "PhotonPtCutForLooseTiming": ["2.0"],
                                      "PhotonTightTimingCut": ["2.5"],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LE_LooseSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorLoose_LE)

CLICPfoSelectorTight_LE = MarlinProcessorWrapper("CLICPfoSelectorTight_LE")
CLICPfoSelectorTight_LE.OutputLevel = INFO
CLICPfoSelectorTight_LE.ProcessorType = "CLICPfoSelector"
CLICPfoSelectorTight_LE.Parameters = {
                                      "ChargedPfoLooseTimingCut": ["4.0"],
                                      "ChargedPfoNegativeLooseTimingCut": ["-2.0"],
                                      "ChargedPfoNegativeTightTimingCut": ["-1.0"],
                                      "ChargedPfoPtCut": ["0.0"],
                                      "ChargedPfoPtCutForLooseTiming": ["3.0"],
                                      "ChargedPfoTightTimingCut": ["2.0"],
                                      "CheckKaonCorrection": ["0"],
                                      "CheckProtonCorrection": ["0"],
                                      "ClusterLessPfoTrackTimeCut": ["10."],
                                      "CorrectHitTimesForTimeOfFlight": ["0"],
                                      "DisplayRejectedPfos": ["1"],
                                      "DisplaySelectedPfos": ["1"],
                                      "FarForwardCosTheta": ["0.975"],
                                      "ForwardCosThetaForHighEnergyNeutralHadrons": ["0.95"],
                                      "ForwardHighEnergyNeutralHadronsEnergy": ["10"],
                                      "HCalBarrelLooseTimingCut": ["4"],
                                      "HCalBarrelTightTimingCut": ["2"],
                                      "HCalEndCapTimingFactor": ["1"],
                                      "InputPfoCollection": ["PandoraPFOs"],
                                      "KeepKShorts": ["1"],
                                      "MaxMomentumForClusterLessPfos": ["5.0"],
                                      "MinECalHitsForTiming": ["5"],
                                      "MinHCalEndCapHitsForTiming": ["5"],
                                      "MinMomentumForClusterLessPfos": ["0.0"],
                                      "MinPtForClusterLessPfos": ["0.75"],
                                      "MinimumEnergyForNeutronTiming": ["1"],
                                      "Monitoring": ["0"],
                                      "MonitoringPfoEnergyToDisplay": ["1"],
                                      "NeutralFarForwardLooseTimingCut": ["2.0"],
                                      "NeutralFarForwardTightTimingCut": ["2.0"],
                                      "NeutralHadronBarrelPtCutForLooseTiming": ["3.5"],
                                      "NeutralHadronLooseTimingCut": ["4.0"],
                                      "NeutralHadronPtCut": ["0.0"],
                                      "NeutralHadronPtCutForLooseTiming": ["3.0"],
                                      "NeutralHadronTightTimingCut": ["2.0"],
                                      "PhotonFarForwardLooseTimingCut": ["2"],
                                      "PhotonFarForwardTightTimingCut": ["1"],
                                      "PhotonLooseTimingCut": ["1.0"],
                                      "PhotonPtCut": ["0.0"],
                                      "PhotonPtCutForLooseTiming": ["2.0"],
                                      "PhotonTightTimingCut": ["1.0"],
                                      "PtCutForTightTiming": ["0.75"],
                                      "SelectedPfoCollection": ["LE_TightSelectedPandoraPFOs"],
                                      "UseClusterLessPfos": ["1"],
                                      "UseNeutronTiming": ["0"]
                                      }
algList.append(CLICPfoSelectorTight_LE)

MyFastJetProcessor = MarlinProcessorWrapper("MyFastJetProcessor")
MyFastJetProcessor.OutputLevel = INFO
MyFastJetProcessor.ProcessorType = "FastJetProcessor"
MyFastJetProcessor.Parameters = {
                                 "algorithm": ["kt_algorithm", "0.5"],
                                 "clusteringMode": ["Inclusive", "5"],
                                 "jetOut": ["JetCaloOut"],
                                 "recParticleIn": ["SelectedPandoraPFOs"],
                                 "recombinationScheme": ["E_scheme"]
                                 }
algList.append(MyFastJetProcessor)

MyLCTuple = MarlinProcessorWrapper("MyLCTuple")
MyLCTuple.OutputLevel = INFO
MyLCTuple.ProcessorType = "LCTuple"
MyLCTuple.Parameters = {
                        "CalorimeterHitCollection": [],
                        "ClusterCollection": ["PandoraClusters"],
                        "FullSubsetCollections": [],
                        "IsoLepCollection": [],
                        "JetCollection": ["JetCaloOut"],
                        "JetCollectionDaughtersParameters": ["true"],
                        "JetCollectionExtraParameters": ["false"],
                        "JetCollectionTaggingParameters": ["false"],
                        "LCRelationCollections": [],
                        "LCRelationPrefixes": [],
                        "LCRelationwithPFOCollections": [],
                        "MCParticleCollection": ["MCPhysicsParticles"],
                        "MCParticleNotReco": [],
                        "RecoParticleCollection": ["PandoraPFOs"],
                        "SimCalorimeterHitCollection": [],
                        "SimTrackerHitCollection": [],
                        "TrackCollection": ["SiTracks_Refitted"],
                        "TrackerHitCollection": [],
                        "VertexCollection": [],
                        "WriteCalorimeterHitCollectionParameters": ["false"],
                        "WriteClusterCollectionParameters": ["false"],
                        "WriteIsoLepCollectionParameters": ["false"],
                        "WriteJetCollectionParameters": ["true"],
                        "WriteMCParticleCollectionParameters": ["false"],
                        "WriteRecoParticleCollectionParameters": ["false"],
                        "WriteSimCalorimeterHitCollectionParameters": ["false"],
                        "WriteSimTrackerHitCollectionParameters": ["false"],
                        "WriteTrackCollectionParameters": ["false"],
                        "WriteTrackerHitCollectionParameters": ["false"],
                        "WriteVertexCollectionParameters": ["false"]
                        }
algList.append(MyLCTuple)

Output_REC = MarlinProcessorWrapper("Output_REC")
Output_REC.OutputLevel = INFO
Output_REC.ProcessorType = "LCIOOutputProcessor"
Output_REC.Parameters = {
                         "DropCollectionNames": ["SeedTracks"],
                         "DropCollectionTypes": [],
                         "FullSubsetCollections": ["EfficientMCParticles", "InefficientMCParticles"],
                         "KeepCollectionNames": [],
                         "LCIOOutputFile": ["output_reco.slcio"],
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

