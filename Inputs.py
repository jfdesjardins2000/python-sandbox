from dataclasses import dataclass
from typing import List

@dataclass
class Objective1:
    ACPFAIBL: float
    ACPFORT: float
    ACPIL: float
    ACPPTM: float
    ACRS: float
    ACT: float
    AEC: float
    AEPC: float
    ANET: float
    APLBA: float
    APLIN: float
    Objective: float
    Primalinfeasibility: float
    Total: float
    AREG: float
    ATBEMORT: float
    ATBERETARD: float
    ACRV: float
    ASNAT: float

@dataclass
class Outputs:
    OVOLTOTREC: List[float]

@dataclass
class Inputs:
    primary: str
    primary_comment: str
    workingdir: str
    workingdir_comment: str
    scenario: str
    scenario_comment: str
    scale: int
    scale_comment: str
    updatefield: str
    updatefield_comment: str
    simulationstartingyear: int
    simulationstartingyear_comment: str
    simulationlength: int
    simulationlength_comment: str
    timestep: int
    timestep_comment: str
    growththeme: int
    growththeme_comment: str
    areafield: str
    areafield_comment: str
    objectives: List['Objective1']
    allpredictornames: List[str]
    objectives_comment: str
    GCBMtransitionlocations: List[str]
    GCBMtransitionlocation_comment: str
    schedules: str
    schedules_comment: str
    outputs: 'Outputs'
    outputs_comment: str
    eventslocation: str
    eventslocation_comment: str
    carbonpredictorspatialoutputs: List[str]
    carbonpredictorspatialoutputs_comment: str
    predictoryields: List[str]
    predictoryields_comment: str
    predictornames: List[str]
    predictornames_comment: str
    allpredictionsnodes: List[List[List[str]]]
    allpredictionsnodes_comment: str
    yields: str