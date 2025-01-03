from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


@dataclass
class AffineTransform:
    """A matrix used to transform the shape.

    ⎡ A00, A01, A02 ⎤ ⎢ A10, A11, A12 ⎥ ⎣ 0,   0,   1   ⎦
    """

    a00: Optional[float] = field(
        default=None,
        metadata={
            "name": "A00",
            "type": "Attribute",
            "required": True,
        },
    )
    a10: Optional[float] = field(
        default=None,
        metadata={
            "name": "A10",
            "type": "Attribute",
            "required": True,
        },
    )
    a01: Optional[float] = field(
        default=None,
        metadata={
            "name": "A01",
            "type": "Attribute",
            "required": True,
        },
    )
    a11: Optional[float] = field(
        default=None,
        metadata={
            "name": "A11",
            "type": "Attribute",
            "required": True,
        },
    )
    a02: Optional[float] = field(
        default=None,
        metadata={
            "name": "A02",
            "type": "Attribute",
            "required": True,
        },
    )
    a12: Optional[float] = field(
        default=None,
        metadata={
            "name": "A12",
            "type": "Attribute",
            "required": True,
        },
    )


class ArcType(Enum):
    HG = "Hg"
    XE = "Xe"
    HG_XE = "HgXe"
    OTHER = "Other"


class BinDataCompression(Enum):
    ZLIB = "zlib"
    BZIP2 = "bzip2"
    NONE = "none"


class Binning(Enum):
    """Represents the number of pixels that are combined to form larger pixels.

    {used:CCD,EMCCD}

    :cvar VALUE_1X1: No binning.
    :cvar VALUE_2X2: 2×2 binning.
    :cvar VALUE_4X4: 4×4 binning.
    :cvar VALUE_8X8: 8×8 binning.
    :cvar OTHER: Other binning value.
    """

    VALUE_1X1 = "1x1"
    VALUE_2X2 = "2x2"
    VALUE_4X4 = "4x4"
    VALUE_8X8 = "8x8"
    OTHER = "Other"


class ChannelAcquisitionMode(Enum):
    WIDE_FIELD = "WideField"
    LASER_SCANNING_CONFOCAL_MICROSCOPY = "LaserScanningConfocalMicroscopy"
    SPINNING_DISK_CONFOCAL = "SpinningDiskConfocal"
    SLIT_SCAN_CONFOCAL = "SlitScanConfocal"
    MULTI_PHOTON_MICROSCOPY = "MultiPhotonMicroscopy"
    STRUCTURED_ILLUMINATION = "StructuredIllumination"
    SINGLE_MOLECULE_IMAGING = "SingleMoleculeImaging"
    TOTAL_INTERNAL_REFLECTION = "TotalInternalReflection"
    FLUORESCENCE_LIFETIME = "FluorescenceLifetime"
    SPECTRAL_IMAGING = "SpectralImaging"
    FLUORESCENCE_CORRELATION_SPECTROSCOPY = (
        "FluorescenceCorrelationSpectroscopy"
    )
    NEAR_FIELD_SCANNING_OPTICAL_MICROSCOPY = (
        "NearFieldScanningOpticalMicroscopy"
    )
    SECOND_HARMONIC_GENERATION_IMAGING = "SecondHarmonicGenerationImaging"
    PALM = "PALM"
    STORM = "STORM"
    STED = "STED"
    TIRF = "TIRF"
    FSM = "FSM"
    LCM = "LCM"
    OTHER = "Other"
    BRIGHT_FIELD = "BrightField"
    SWEPT_FIELD_CONFOCAL = "SweptFieldConfocal"
    SPIM = "SPIM"


class ChannelContrastMethod(Enum):
    BRIGHTFIELD = "Brightfield"
    PHASE = "Phase"
    DIC = "DIC"
    HOFFMAN_MODULATION = "HoffmanModulation"
    OBLIQUE_ILLUMINATION = "ObliqueIllumination"
    POLARIZED_LIGHT = "PolarizedLight"
    DARKFIELD = "Darkfield"
    FLUORESCENCE = "Fluorescence"
    OTHER = "Other"


class ChannelIlluminationType(Enum):
    TRANSMITTED = "Transmitted"
    EPIFLUORESCENCE = "Epifluorescence"
    OBLIQUE = "Oblique"
    NON_LINEAR = "NonLinear"
    OTHER = "Other"


class DetectorType(Enum):
    CCD = "CCD"
    INTENSIFIED_CCD = "IntensifiedCCD"
    ANALOG_VIDEO = "AnalogVideo"
    PMT = "PMT"
    PHOTODIODE = "Photodiode"
    SPECTROSCOPY = "Spectroscopy"
    LIFETIME_IMAGING = "LifetimeImaging"
    CORRELATION_SPECTROSCOPY = "CorrelationSpectroscopy"
    FTIR = "FTIR"
    EMCCD = "EMCCD"
    APD = "APD"
    CMOS = "CMOS"
    EBCCD = "EBCCD"
    OTHER = "Other"


class ExperimentValue(Enum):
    FP = "FP"
    FRET = "FRET"
    TIME_LAPSE = "TimeLapse"
    FOUR_DPLUS = "FourDPlus"
    SCREEN = "Screen"
    IMMUNOCYTOCHEMISTRY = "Immunocytochemistry"
    IMMUNOFLUORESCENCE = "Immunofluorescence"
    FISH = "FISH"
    ELECTROPHYSIOLOGY = "Electrophysiology"
    ION_IMAGING = "IonImaging"
    COLOCALIZATION = "Colocalization"
    PGIDOCUMENTATION = "PGIDocumentation"
    FLUORESCENCE_LIFETIME = "FluorescenceLifetime"
    SPECTRAL_IMAGING = "SpectralImaging"
    PHOTOBLEACHING = "Photobleaching"
    SPIM = "SPIM"
    OTHER = "Other"


class ExternalCompression(Enum):
    ZLIB = "zlib"
    BZIP2 = "bzip2"
    NONE = "none"


class FilamentType(Enum):
    INCANDESCENT = "Incandescent"
    HALOGEN = "Halogen"
    OTHER = "Other"


class FilterType(Enum):
    DICHROIC = "Dichroic"
    LONG_PASS = "LongPass"
    SHORT_PASS = "ShortPass"
    BAND_PASS = "BandPass"
    MULTI_PASS = "MultiPass"
    NEUTRAL_DENSITY = "NeutralDensity"
    TUNEABLE = "Tuneable"
    OTHER = "Other"


class LaserLaserMedium(Enum):
    CU = "Cu"
    AG = "Ag"
    AR_FL = "ArFl"
    AR_CL = "ArCl"
    KR_FL = "KrFl"
    KR_CL = "KrCl"
    XE_FL = "XeFl"
    XE_CL = "XeCl"
    XE_BR = "XeBr"
    N = "N"
    AR = "Ar"
    KR = "Kr"
    XE = "Xe"
    HE_NE = "HeNe"
    HE_CD = "HeCd"
    CO = "CO"
    CO2 = "CO2"
    H2_O = "H2O"
    HFL = "HFl"
    ND_GLASS = "NdGlass"
    ND_YAG = "NdYAG"
    ER_GLASS = "ErGlass"
    ER_YAG = "ErYAG"
    HO_YLF = "HoYLF"
    HO_YAG = "HoYAG"
    RUBY = "Ruby"
    TI_SAPPHIRE = "TiSapphire"
    ALEXANDRITE = "Alexandrite"
    RHODAMINE6_G = "Rhodamine6G"
    COUMARIN_C30 = "CoumarinC30"
    GA_AS = "GaAs"
    GA_AL_AS = "GaAlAs"
    EMINUS = "EMinus"
    OTHER = "Other"


class LaserPulse(Enum):
    CW = "CW"
    SINGLE = "Single"
    QSWITCHED = "QSwitched"
    REPETITIVE = "Repetitive"
    MODE_LOCKED = "ModeLocked"
    OTHER = "Other"


class LaserType(Enum):
    EXCIMER = "Excimer"
    GAS = "Gas"
    METAL_VAPOR = "MetalVapor"
    SOLID_STATE = "SolidState"
    DYE = "Dye"
    SEMICONDUCTOR = "Semiconductor"
    FREE_ELECTRON = "FreeElectron"
    OTHER = "Other"


@dataclass
class ManufacturerSpec:
    """This is the base from which many microscope components are extended.

    E.g Objective, Filter etc. Provides attributes for recording common
    properties of these components such as Manufacturer name, Model etc,
    all of which are optional.

    :ivar manufacturer: The manufacturer of the component. [plain text
        string]
    :ivar model: The Model of the component. [plain text string]
    :ivar serial_number: The serial number of the component. [plain text
        string]
    :ivar lot_number: The lot number of the component. [plain text
        string]
    """

    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Attribute",
        },
    )
    model: Optional[str] = field(
        default=None,
        metadata={
            "name": "Model",
            "type": "Attribute",
        },
    )
    serial_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "SerialNumber",
            "type": "Attribute",
        },
    )
    lot_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "LotNumber",
            "type": "Attribute",
        },
    )


@dataclass
class Map:
    """
    This is a Mapping of key/value pairs.

    :ivar m: This is a key/value pair used to build up a Mapping. The
        Element and Attribute name are kept to single letters to
        minimize the length at the expense of readability as they are
        likely to occur many times.
    """

    m: list["Map.M"] = field(
        default_factory=list,
        metadata={
            "name": "M",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )

    @dataclass
    class M:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        k: Optional[str] = field(
            default=None,
            metadata={
                "name": "K",
                "type": "Attribute",
            },
        )


class Marker(Enum):
    """Shape of marker on the end of a line.

    [enumeration]
    """

    ARROW = "Arrow"


@dataclass
class MetadataOnly:
    """
    This place holder means there is on pixel data in this file.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


class MicrobeamManipulationValue(Enum):
    FRAP = "FRAP"
    FLIP = "FLIP"
    INVERSE_FRAP = "InverseFRAP"
    PHOTOABLATION = "Photoablation"
    PHOTOACTIVATION = "Photoactivation"
    UNCAGING = "Uncaging"
    OPTICAL_TRAPPING = "OpticalTrapping"
    OTHER = "Other"


class MicroscopeType(Enum):
    UPRIGHT = "Upright"
    INVERTED = "Inverted"
    DISSECTION = "Dissection"
    ELECTROPHYSIOLOGY = "Electrophysiology"
    OTHER = "Other"


class NamingConvention(Enum):
    """
    Predefined list of values for the well labels.

    :cvar LETTER: While the label type 'number' has a clear meaning the
        'letter' type is more complex. If you have less than 26 values
        use letters A to Z. Once you get more than 26 values there are
        several different approaches in use. One we have see include:
        Single letter, then double letter each running A to Z, right
        first e.g. A, B, C, ... X, Y, Z, AA, AB, AC, ... AY, AZ, BA, BB,
        ... This is the format used by Microsoft Excel so users may be
        familiar with it. This is the approach we use in the OMERO
        client applications. CAPITALsmall, each running A to Z, small
        first e.g. Aa, Ab, Ac, ... Ax, Ay, Az, Ba, Bb, Bc, ... By, Bz,
        Ca, Cb, ... This is in use by some plate manufactures. Single
        letter, then double letter, then triple letter, and so on e.g.
        A, B, C, ... X, Y, Z, AA, BB, CC, ... YY, ZZ, AAA, BBB, ... This
        has the advantage that the first 26 are the same as the standard
        but has a problem an the labels get wider and wider leading to
        user interface problems.
    :cvar NUMBER: 1, 2, 3, ...
    """

    LETTER = "letter"
    NUMBER = "number"


class ObjectiveSettingsMedium(Enum):
    """A description of a Medium used for the lens.

    The Medium is the actual immersion medium used in this case.
    """

    AIR = "Air"
    OIL = "Oil"
    WATER = "Water"
    GLYCEROL = "Glycerol"
    OTHER = "Other"


class ObjectiveCorrection(Enum):
    UV = "UV"
    PLAN_APO = "PlanApo"
    PLAN_FLUOR = "PlanFluor"
    SUPER_FLUOR = "SuperFluor"
    VIOLET_CORRECTED = "VioletCorrected"
    ACHRO = "Achro"
    ACHROMAT = "Achromat"
    FLUOR = "Fluor"
    FL = "Fl"
    FLUAR = "Fluar"
    NEOFLUAR = "Neofluar"
    FLUOTAR = "Fluotar"
    APO = "Apo"
    PLAN_NEOFLUAR = "PlanNeofluar"
    OTHER = "Other"


class ObjectiveImmersion(Enum):
    OIL = "Oil"
    WATER = "Water"
    WATER_DIPPING = "WaterDipping"
    AIR = "Air"
    MULTI = "Multi"
    GLYCEROL = "Glycerol"
    OTHER = "Other"


class PixelType(Enum):
    """
    The number size/kind used to represent a pixel.

    :cvar INT8: 8 bit signed integer.
    :cvar INT16: 16 bit signed integer.
    :cvar INT32: 32 bit signed integer.
    :cvar UINT8: 8 bit unsigned integer.
    :cvar UINT16: 16 bit unsigned integer.
    :cvar UINT32: 32 bit unsigned integer.
    :cvar FLOAT: single-precision floating point.
    :cvar DOUBLE: double-precision floating point.
    :cvar COMPLEX: complex single-precision floating point.
    :cvar DOUBLE_COMPLEX: complex double-precision floating point.
    :cvar BIT: bit mask.
    """

    INT8 = "int8"
    INT16 = "int16"
    INT32 = "int32"
    UINT8 = "uint8"
    UINT16 = "uint16"
    UINT32 = "uint32"
    FLOAT = "float"
    DOUBLE = "double"
    COMPLEX = "complex"
    DOUBLE_COMPLEX = "double-complex"
    BIT = "bit"


class PixelsDimensionOrder(Enum):
    XYZCT = "XYZCT"
    XYZTC = "XYZTC"
    XYCTZ = "XYCTZ"
    XYCZT = "XYCZT"
    XYTCZ = "XYTCZ"
    XYTZC = "XYTZC"


@dataclass
class Reference:
    """
    Reference is an empty complex type that is contained and extended by all the
    *Ref elements and also the Settings Complex Type Each *Ref element defines an
    attribute named ID of simple type *ID and no other information Each simple type
    *ID is restricted to the base type LSID with an appropriate pattern.
    """


@dataclass
class Rights:
    """
    The rights holder of this data and the rights held.

    :ivar rights_holder: The rights holder for this data. [plain-text
        multi-line string] e.g. "Copyright (C) 2002 - 2016 Open
        Microscopy Environment"
    :ivar rights_held: The rights held by the rights holder. [plain-text
        multi-line string] e.g. "All rights reserved" or "Creative
        Commons Attribution 3.0 Unported License"
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    rights_holder: Optional[str] = field(
        default=None,
        metadata={
            "name": "RightsHolder",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    rights_held: Optional[str] = field(
        default=None,
        metadata={
            "name": "RightsHeld",
            "type": "Element",
            "white_space": "preserve",
        },
    )


class ShapeFillRule(Enum):
    """The rule used to decide which parts of the shape to fill.

    [enumeration]
    """

    EVEN_ODD = "EvenOdd"
    NON_ZERO = "NonZero"


class ShapeFontFamily(Enum):
    """The font family used to draw the text.

    [enumeration]
    Note: these values are all lower case so they match
    the standard HTML/CSS values. "fantasy" has been
    included for completeness; we do not recommend its
    regular use. This attribute is under consideration
    for removal from the OME-XML schema.
    """

    SERIF = "serif"
    SANS_SERIF = "sans-serif"
    CURSIVE = "cursive"
    FANTASY = "fantasy"
    MONOSPACE = "monospace"


class ShapeFontStyle(Enum):
    """The style and weight applied to the text.

    [enumeration] This is a simplified combination of the HTML/CSS
    attributes font-style AND font-weight.
    """

    BOLD = "Bold"
    BOLD_ITALIC = "BoldItalic"
    ITALIC = "Italic"
    NORMAL = "Normal"


@dataclass
class TiffData:
    """
    This described the location of the pixel data in a tiff file.

    :ivar uuid: This must be used when the IFDs are located in another
        file. Note: It is permissible for this to be self referential.
    :ivar ifd: Gives the IFD(s) for which this element is applicable.
        Indexed from 0. Default is 0 (the first IFD). [units:none]
    :ivar first_z: Gives the Z position of the image plane at the
        specified IFD. Indexed from 0. Default is 0 (the first Z
        position). [units:none]
    :ivar first_t: Gives the T position of the image plane at the
        specified IFD. Indexed from 0. Default is 0 (the first T
        position). [units:none]
    :ivar first_c: Gives the C position of the image plane at the
        specified IFD. Indexed from 0. Default is 0 (the first C
        position). [units:none]
    :ivar plane_count: Gives the number of IFDs affected. Dimension
        order of IFDs is given by the enclosing Pixels element's
        DimensionOrder attribute. Default is the number of IFDs in the
        TIFF file, unless an IFD is specified, in which case the default
        is 1. [units:none]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    uuid: Optional["TiffData.Uuid"] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Element",
        },
    )
    ifd: int = field(
        default=0,
        metadata={
            "name": "IFD",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    first_z: int = field(
        default=0,
        metadata={
            "name": "FirstZ",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    first_t: int = field(
        default=0,
        metadata={
            "name": "FirstT",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    first_c: int = field(
        default=0,
        metadata={
            "name": "FirstC",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    plane_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "PlaneCount",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )

    @dataclass
    class Uuid:
        """
        :ivar value:
        :ivar file_name: This can be used when the IFDs are located in
            another file. The / (forward slash) is used as the path
            separator. A relative path is recommended. However an
            absolute path can be specified. Default is to use the file
            the ome-xml data has been pulled from. Note: It is
            permissible for this to be self referential. The file
            image1.tiff may contain ome-xml data that has
            FilePath="image1.tiff" or "./image1.tiff"
        """

        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r"(urn:uuid:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})",
            },
        )
        file_name: Optional[str] = field(
            default=None,
            metadata={
                "name": "FileName",
                "type": "Attribute",
            },
        )


class UnitsElectricPotential(Enum):
    """
    The units used to represent an electric potential.

    :cvar YV: yottavolt unit.
    :cvar ZV: zettavolt unit.
    :cvar EV: exavolt unit.
    :cvar PV: petavolt unit.
    :cvar TV: teravolt unit.
    :cvar GV: gigavolt unit.
    :cvar MV: megavolt unit.
    :cvar K_V: kilovolt unit.
    :cvar H_V: hectovolt unit.
    :cvar DA_V: decavolt unit.
    :cvar V: volt unit.
    :cvar D_V: decivolt unit.
    :cvar C_V: centivolt unit.
    :cvar M_V_1: millivolt unit.
    :cvar V_1: microvolt unit.
    :cvar N_V: nanovolt unit.
    :cvar P_V_1: picovolt unit.
    :cvar F_V: femtovolt unit.
    :cvar A_V: attovolt unit.
    :cvar Z_V_1: zeptovolt unit.
    :cvar Y_V_1: yoctovolt unit.
    """

    YV = "YV"
    ZV = "ZV"
    EV = "EV"
    PV = "PV"
    TV = "TV"
    GV = "GV"
    MV = "MV"
    K_V = "kV"
    H_V = "hV"
    DA_V = "daV"
    V = "V"
    D_V = "dV"
    C_V = "cV"
    M_V_1 = "mV"
    V_1 = "µV"
    N_V = "nV"
    P_V_1 = "pV"
    F_V = "fV"
    A_V = "aV"
    Z_V_1 = "zV"
    Y_V_1 = "yV"


class UnitsFrequency(Enum):
    """
    The units used to represent frequency.

    :cvar YHZ: yottahertz unit.
    :cvar ZHZ: zettahertz unit.
    :cvar EHZ: exahertz unit.
    :cvar PHZ: petahertz unit.
    :cvar THZ: terahertz unit.
    :cvar GHZ: gigahertz unit.
    :cvar MHZ: megahertz unit.
    :cvar K_HZ: kilohertz unit.
    :cvar H_HZ: hectohertz unit.
    :cvar DA_HZ: decahertz unit.
    :cvar HZ: hertz unit.
    :cvar D_HZ: decihertz unit.
    :cvar C_HZ: centihertz unit.
    :cvar M_HZ_1: millihertz unit.
    :cvar HZ_1: microhertz unit.
    :cvar N_HZ: nanohertz unit.
    :cvar P_HZ_1: picohertz unit.
    :cvar F_HZ: femtohertz unit.
    :cvar A_HZ: attohertz unit.
    :cvar Z_HZ_1: zeptohertz unit.
    :cvar Y_HZ_1: yoctohertz unit.
    """

    YHZ = "YHz"
    ZHZ = "ZHz"
    EHZ = "EHz"
    PHZ = "PHz"
    THZ = "THz"
    GHZ = "GHz"
    MHZ = "MHz"
    K_HZ = "kHz"
    H_HZ = "hHz"
    DA_HZ = "daHz"
    HZ = "Hz"
    D_HZ = "dHz"
    C_HZ = "cHz"
    M_HZ_1 = "mHz"
    HZ_1 = "µHz"
    N_HZ = "nHz"
    P_HZ_1 = "pHz"
    F_HZ = "fHz"
    A_HZ = "aHz"
    Z_HZ_1 = "zHz"
    Y_HZ_1 = "yHz"


class UnitsLength(Enum):
    """
    The units used to represent a length.

    :cvar YM: yottameter SI unit.
    :cvar ZM: zettameter SI unit.
    :cvar EM: exameter SI unit.
    :cvar PM: petameter SI unit.
    :cvar TM: terameter SI unit.
    :cvar GM: gigameter SI unit.
    :cvar MM: megameter SI unit.
    :cvar KM: kilometer SI unit.
    :cvar HM: hectometer SI unit.
    :cvar DAM: decameter SI unit.
    :cvar M: meter SI unit.
    :cvar DM: decimeter SI unit.
    :cvar CM: centimeter SI unit.
    :cvar MM_1: millimeter SI unit.
    :cvar M_1: micrometer SI unit.
    :cvar NM: nanometer SI unit.
    :cvar PM_1: picometer SI unit.
    :cvar FM: femtometer SI unit.
    :cvar AM: attometer SI unit.
    :cvar ZM_1: zeptometer SI unit.
    :cvar YM_1: yoctometer SI unit.
    :cvar LATIN_CAPITAL_LETTER_A_WITH_RING_ABOVE: ångström SI-derived
        unit.
    :cvar THOU: thou Imperial unit (or mil, 1/1000 inch).
    :cvar LI: line Imperial unit (1/12 inch).
    :cvar IN: inch Imperial unit.
    :cvar FT: foot Imperial unit.
    :cvar YD: yard Imperial unit.
    :cvar MI: terrestrial mile Imperial unit.
    :cvar UA: astronomical unit SI-derived unit. The official term is ua
        as the SI standard assigned AU to absorbance unit.
    :cvar LY: light year.
    :cvar PC: parsec.
    :cvar PT: typography point Imperial-derived unit (1/72 inch). Use of
        this unit should be limited to font sizes.
    :cvar PIXEL: pixel abstract unit.  This is not convertible to any
        other length unit without a calibrated scaling factor. Its use
        should should be limited to ROI objects, and converted to an
        appropriate length units using the PhysicalSize units of the
        Image the ROI is attached to.
    :cvar REFERENCE_FRAME: reference frame abstract unit.  This is not
        convertible to any other length unit without a scaling factor.
        Its use should be limited to uncalibrated stage positions, and
        converted to an appropriate length unit using a calibrated
        scaling factor.
    """

    YM = "Ym"
    ZM = "Zm"
    EM = "Em"
    PM = "Pm"
    TM = "Tm"
    GM = "Gm"
    MM = "Mm"
    KM = "km"
    HM = "hm"
    DAM = "dam"
    M = "m"
    DM = "dm"
    CM = "cm"
    MM_1 = "mm"
    M_1 = "µm"
    NM = "nm"
    PM_1 = "pm"
    FM = "fm"
    AM = "am"
    ZM_1 = "zm"
    YM_1 = "ym"
    LATIN_CAPITAL_LETTER_A_WITH_RING_ABOVE = "Å"
    THOU = "thou"
    LI = "li"
    IN = "in"
    FT = "ft"
    YD = "yd"
    MI = "mi"
    UA = "ua"
    LY = "ly"
    PC = "pc"
    PT = "pt"
    PIXEL = "pixel"
    REFERENCE_FRAME = "reference frame"


class UnitsPower(Enum):
    """
    The units used to represent power.

    :cvar YW: yottawatt unit.
    :cvar ZW: zettawatt unit.
    :cvar EW: exawatt unit.
    :cvar PW: petawatt unit.
    :cvar TW: terawatt unit.
    :cvar GW: gigawatt unit.
    :cvar MW: megawatt unit.
    :cvar K_W: kilowatt unit.
    :cvar H_W: hectowatt unit.
    :cvar DA_W: decawatt unit.
    :cvar W: watt unit.
    :cvar D_W: deciwatt unit.
    :cvar C_W: centiwatt unit.
    :cvar M_W_1: milliwatt unit.
    :cvar W_1: microwatt unit.
    :cvar N_W: nanowatt unit.
    :cvar P_W_1: picowatt unit.
    :cvar F_W: femtowatt unit.
    :cvar A_W: attowatt unit.
    :cvar Z_W_1: zeptowatt unit.
    :cvar Y_W_1: yoctowatt unit.
    """

    YW = "YW"
    ZW = "ZW"
    EW = "EW"
    PW = "PW"
    TW = "TW"
    GW = "GW"
    MW = "MW"
    K_W = "kW"
    H_W = "hW"
    DA_W = "daW"
    W = "W"
    D_W = "dW"
    C_W = "cW"
    M_W_1 = "mW"
    W_1 = "µW"
    N_W = "nW"
    P_W_1 = "pW"
    F_W = "fW"
    A_W = "aW"
    Z_W_1 = "zW"
    Y_W_1 = "yW"


class UnitsPressure(Enum):
    """
    The units used to represent a pressure.

    :cvar YPA: yottapascal SI unit.
    :cvar ZPA: zettapascal SI unit.
    :cvar EPA: exapascal SI unit.
    :cvar PPA: petapascal SI unit.
    :cvar TPA: terapascal SI unit.
    :cvar GPA: gigapascal SI unit.
    :cvar MPA: megapascal SI unit.
    :cvar K_PA: kilopascal SI unit.
    :cvar H_PA: hectopascal SI unit.
    :cvar DA_PA: decapascal SI unit.
    :cvar PA: pascal SI unit.  Note the C++ enum is mixed case due to
        PASCAL being a macro used by the Microsoft C and C++ compiler.
    :cvar D_PA: decipascal SI unit.
    :cvar C_PA: centipascal SI unit.
    :cvar M_PA_1: millipascal SI unit.
    :cvar PA_1: micropascal SI unit.
    :cvar N_PA: nanopascal SI unit.
    :cvar P_PA_1: picopascal SI unit.
    :cvar F_PA: femtopascal SI unit.
    :cvar A_PA: attopascal SI unit.
    :cvar Z_PA_1: zeptopascal SI unit.
    :cvar Y_PA_1: yoctopascal SI unit.
    :cvar BAR: bar SI-derived unit.
    :cvar MBAR: megabar SI-derived unit.
    :cvar KBAR: kilobar SI-derived unit.
    :cvar DBAR: decibar SI-derived unit.
    :cvar CBAR: centibar SI-derived unit.
    :cvar MBAR_1: millibar SI-derived unit.
    :cvar ATM: standard atmosphere SI-derived unit.
    :cvar PSI: pound-force per square inch Imperial unit.
    :cvar TORR: torr SI-derived unit.
    :cvar M_TORR: millitorr SI-derived unit.
    :cvar MM_HG: millimetre of mercury SI-derived unit
    """

    YPA = "YPa"
    ZPA = "ZPa"
    EPA = "EPa"
    PPA = "PPa"
    TPA = "TPa"
    GPA = "GPa"
    MPA = "MPa"
    K_PA = "kPa"
    H_PA = "hPa"
    DA_PA = "daPa"
    PA = "Pa"
    D_PA = "dPa"
    C_PA = "cPa"
    M_PA_1 = "mPa"
    PA_1 = "µPa"
    N_PA = "nPa"
    P_PA_1 = "pPa"
    F_PA = "fPa"
    A_PA = "aPa"
    Z_PA_1 = "zPa"
    Y_PA_1 = "yPa"
    BAR = "bar"
    MBAR = "Mbar"
    KBAR = "kbar"
    DBAR = "dbar"
    CBAR = "cbar"
    MBAR_1 = "mbar"
    ATM = "atm"
    PSI = "psi"
    TORR = "Torr"
    M_TORR = "mTorr"
    MM_HG = "mm Hg"


class UnitsTemperature(Enum):
    """
    The units used to represent a temperature.

    :cvar C: degree Celsius unit.
    :cvar F: degree Fahrenheit unit.
    :cvar K: Kelvin unit.
    :cvar R: degree Rankine unit.
    """

    C = "°C"
    F = "°F"
    K = "K"
    R = "°R"


class UnitsTime(Enum):
    """
    The units used to represent a time interval.

    :cvar YS: yottasecond SI unit.
    :cvar ZS: zettasecond SI unit.
    :cvar ES: exasecond SI unit.
    :cvar PS: petasecond SI unit.
    :cvar TS: terasecond SI unit.
    :cvar GS: gigasecond SI unit.
    :cvar MS: megasecond SI unit.
    :cvar KS: kilosecond SI unit.
    :cvar HS: hectosecond SI unit.
    :cvar DAS: decasecond SI unit.
    :cvar S: second SI unit.
    :cvar DS: decisecond SI unit.
    :cvar CS: centisecond SI unit.
    :cvar MS_1: millisecond SI unit.
    :cvar S_1: microsecond SI unit.
    :cvar NS: nanosecond SI unit.
    :cvar PS_1: picosecond SI unit.
    :cvar FS: femtosecond SI unit.
    :cvar AS: attosecond SI unit.
    :cvar ZS_1: zeptosecond SI unit.
    :cvar YS_1: yoctosecond SI unit.
    :cvar MIN: minute SI-derived unit.
    :cvar H: hour SI-derived unit.
    :cvar D: day SI-derived unit.
    """

    YS = "Ys"
    ZS = "Zs"
    ES = "Es"
    PS = "Ps"
    TS = "Ts"
    GS = "Gs"
    MS = "Ms"
    KS = "ks"
    HS = "hs"
    DAS = "das"
    S = "s"
    DS = "ds"
    CS = "cs"
    MS_1 = "ms"
    S_1 = "µs"
    NS = "ns"
    PS_1 = "ps"
    FS = "fs"
    AS = "as"
    ZS_1 = "zs"
    YS_1 = "ys"
    MIN = "min"
    H = "h"
    D = "d"


@dataclass
class AnnotationRef(Reference):
    """
    The AnnotationRef element is a reference to an element derived from the
    CommonAnnotation element.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Annotation:\S+)|(Annotation:\S+)",
        },
    )


@dataclass
class BinData:
    """The contents of this element are base64-encoded.

    These are not CDATA sections, just a base64 stream.

    :ivar value:
    :ivar compression: Specifies the compression scheme used to encode
        the data.
    :ivar big_endian: This is true if the binary data was written in
        BigEndian order. This is dependent on the system architecture of
        the machine that wrote the pixels. True for essentially all
        modern CPUs other than Intel and Alpha. All Binary data must be
        written in the same endian order.
    :ivar length: Character count attribute for the BinData field. This
        is the length of the base-64 encoded block. It allows easy
        skipping of the block when parsing the file. [unit:bytes]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[bytes] = field(
        default=None,
        metadata={
            "required": True,
            "format": "base64",
        },
    )
    compression: BinDataCompression = field(
        default=BinDataCompression.NONE,
        metadata={
            "name": "Compression",
            "type": "Attribute",
        },
    )
    big_endian: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BigEndian",
            "type": "Attribute",
            "required": True,
        },
    )
    length: Optional[int] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )


@dataclass
class ChannelRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Channel:\S+)|(Channel:\S+)",
        },
    )


@dataclass
class DatasetRef(Reference):
    """The DatasetRef element refers to a Dataset by specifying the Dataset ID
    attribute.

    One or more DatasetRef elements may be listed within the Image
    element to specify what Datasets the Image belongs to.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Dataset:\S+)|(Dataset:\S+)",
        },
    )


@dataclass
class DichroicRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Dichroic:\S+)|(Dichroic:\S+)",
        },
    )


@dataclass
class ExperimentRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experiment:\S+)|(Experiment:\S+)",
        },
    )


@dataclass
class ExperimenterGroupRef(Reference):
    """
    This empty element has a reference (the ExperimenterGroup ID attribute) to a
    ExperimenterGroup defined within OME.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:ExperimenterGroup:\S+)|(ExperimenterGroup:\S+)",
        },
    )


@dataclass
class ExperimenterRef(Reference):
    """
    This empty element has a required Experimenter ID and an optional DocumentID
    attribute which refers to one of the Experimenters defined within OME.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experimenter:\S+)|(Experimenter:\S+)",
        },
    )


@dataclass
class External:
    """Describes a file location.

    Can optionally specify a portion of a file using Offset and a
    ReadLength. If Offset and ReadLength are specified in conjuction
    with Compression, then they point into the uncompressed file.

    :ivar href: file location
    :ivar sha1: The digest of the file specified in href.
    :ivar compression: Specifies the compression scheme used to encode
        the data.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    sha1: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "SHA1",
            "type": "Attribute",
            "required": True,
            "length": 20,
            "format": "base16",
        },
    )
    compression: ExternalCompression = field(
        default=ExternalCompression.NONE,
        metadata={
            "name": "Compression",
            "type": "Attribute",
        },
    )


@dataclass
class FilterRef(Reference):
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Filter:\S+)|(Filter:\S+)",
        },
    )


@dataclass
class FilterSetRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:FilterSet:\S+)|(FilterSet:\S+)",
        },
    )


@dataclass
class FolderRef(Reference):
    """The FolderRef element refers to a Folder by specifying the Folder ID
    attribute.

    One or more FolderRef elements may be listed within the Folder
    element to specify what Folders the Folder contains. This tree
    hierarchy must be acyclic.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Folder:\S+)|(Folder:\S+)",
        },
    )


@dataclass
class ImageRef(Reference):
    """
    The ImageRef element is a reference to an Image element.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Image:\S+)|(Image:\S+)",
        },
    )


@dataclass
class ImagingEnvironment:
    """
    This describes the environment that the biological sample was in during the
    experiment.

    :ivar map:
    :ivar temperature: The Temperature is the define units.
    :ivar temperature_unit: The units the Temperature is in -
        default:Celsius[°C].
    :ivar air_pressure: AirPressure is the define units.
    :ivar air_pressure_unit: The units the AirPressure is in -
        default:millibars[mbar].
    :ivar humidity: Humidity around the sample [units:none] A fraction,
        as a value from 0.0 to 1.0.
    :ivar co2_percent: Carbon Dioxide concentration around the sample
        [units:none] A fraction, as a value from 0.0 to 1.0.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    map: Optional[Map] = field(
        default=None,
        metadata={
            "name": "Map",
            "type": "Element",
        },
    )
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "name": "Temperature",
            "type": "Attribute",
        },
    )
    temperature_unit: UnitsTemperature = field(
        default=UnitsTemperature.C,
        metadata={
            "name": "TemperatureUnit",
            "type": "Attribute",
        },
    )
    air_pressure: Optional[float] = field(
        default=None,
        metadata={
            "name": "AirPressure",
            "type": "Attribute",
        },
    )
    air_pressure_unit: UnitsPressure = field(
        default=UnitsPressure.MBAR_1,
        metadata={
            "name": "AirPressureUnit",
            "type": "Attribute",
        },
    )
    humidity: Optional[float] = field(
        default=None,
        metadata={
            "name": "Humidity",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    co2_percent: Optional[float] = field(
        default=None,
        metadata={
            "name": "CO2Percent",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass
class InstrumentRef(Reference):
    """
    This empty element can be used (via the required Instrument ID attribute) to
    refer to an Instrument defined within OME.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Instrument:\S+)|(Instrument:\S+)",
        },
    )


@dataclass
class Leader(Reference):
    """
    Contact information for a ExperimenterGroup leader specified using a reference
    to an Experimenter element defined elsewhere in the document.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experimenter:\S+)|(Experimenter:\S+)",
        },
    )


@dataclass
class MicrobeamManipulationRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:MicrobeamManipulation:\S+)|(MicrobeamManipulation:\S+)",
        },
    )


@dataclass
class Microscope(ManufacturerSpec):
    """
    The microscope's manufacturer specification.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    type_value: Optional[MicroscopeType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class ProjectRef(Reference):
    """There may be one or more of these in a Dataset.

    This empty element has a required Project ID attribute that refers
    to Projects defined within the OME element.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Project:\S+)|(Project:\S+)",
        },
    )


@dataclass
class Pump(Reference):
    """The Pump element is a reference to a LightSource.

    It is used within the Laser element to specify the light source for
    the laser's pump (if any).
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:LightSource:\S+)|(LightSource:\S+)",
        },
    )


@dataclass
class Roiref(Reference):
    class Meta:
        name = "ROIRef"
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:\S+)|(\S+)",
        },
    )


@dataclass
class ReagentRef(Reference):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Reagent:\S+)|(Reagent:\S+)",
        },
    )


@dataclass
class Settings(Reference):
    """Settings is an empty complex type that is contained and extended by all the
    *Settings elements Each *Settings element defines an attribute named ID of
    simple type *ID and the other information that is needed.

    Each simple type *ID is restricted to the base type LSID with an
    appropriate pattern
    """


@dataclass
class StageLabel:
    """
    The StageLabel is used to specify a name and position for a stage position in
    the microscope's reference frame.

    :ivar name:
    :ivar x: The X position of the stage label. Units are set by XUnit.
    :ivar xunit: The units of the X stage position - default:[reference
        frame].
    :ivar y: The Y position of the stage label. Units are set by YUnit.
    :ivar yunit: The units of the Y stage position - default:[reference
        frame].
    :ivar z: The Z position of the stage label. Units are set by ZUnit.
    :ivar zunit: The units of the Z  stage position - default:[reference
        frame].
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
        },
    )
    xunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "XUnit",
            "type": "Attribute",
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
        },
    )
    yunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "YUnit",
            "type": "Attribute",
        },
    )
    z: Optional[float] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Attribute",
        },
    )
    zunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "ZUnit",
            "type": "Attribute",
        },
    )


@dataclass
class TransmittanceRange:
    """This records the range of wavelengths that are transmitted by the filter.

    It also records the maximum amount of light transmitted.

    :ivar cut_in: CutIn is the wavelength below which there is less than
        50% transmittance for a filter. Units are set by CutInUnit.
    :ivar cut_in_unit: The units of the CutIn - default:nanometres[nm].
    :ivar cut_out: CutOut is the wavelength above which there is less
        than 50% transmittance for a filter. Units are set by
        CutOutUnit.
    :ivar cut_out_unit: The units of the CutOut -
        default:nanometres[nm].
    :ivar cut_in_tolerance: CutInTolerance. Units are set by
        CutInToleranceUnit.
    :ivar cut_in_tolerance_unit: The units of the CutInTolerance -
        default:nanometres[nm].
    :ivar cut_out_tolerance: CutOutTolerance. Units are set by
        CutOutToleranceUnit.
    :ivar cut_out_tolerance_unit: The units of the CutOutTolerance -
        default:nanometres[nm].
    :ivar transmittance: The amount of light the filter transmits at a
        maximum [units:none] A fraction, as a value from 0.0 to 1.0.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    cut_in: Optional[float] = field(
        default=None,
        metadata={
            "name": "CutIn",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    cut_in_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "CutInUnit",
            "type": "Attribute",
        },
    )
    cut_out: Optional[float] = field(
        default=None,
        metadata={
            "name": "CutOut",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    cut_out_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "CutOutUnit",
            "type": "Attribute",
        },
    )
    cut_in_tolerance: Optional[float] = field(
        default=None,
        metadata={
            "name": "CutInTolerance",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    cut_in_tolerance_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "CutInToleranceUnit",
            "type": "Attribute",
        },
    )
    cut_out_tolerance: Optional[float] = field(
        default=None,
        metadata={
            "name": "CutOutTolerance",
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    cut_out_tolerance_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "CutOutToleranceUnit",
            "type": "Attribute",
        },
    )
    transmittance: Optional[float] = field(
        default=None,
        metadata={
            "name": "Transmittance",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass
class WellSampleRef(Reference):
    """
    The WellSampleRef element is a reference to a WellSample element.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:WellSample:\S+)|(WellSample:\S+)",
        },
    )


@dataclass
class Annotation:
    """
    An annotation from which all others are ultimately derived.

    :ivar description: A description for the annotation. [plain-text
        multi-line string]
    :ivar annotation_ref:
    :ivar id:
    :ivar namespace: We recommend the inclusion of a namespace for
        annotations you define. If it is absent then we assume the
        annotation is to use our (OME's) default interpretation for this
        type.
    :ivar annotator: The Annotator is the person who attached this
        annotation. e.g. If UserA annotates something with TagB, owned
        by UserB, UserA is still the Annotator.
    """

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
            "white_space": "preserve",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Annotation:\S+)|(Annotation:\S+)",
        },
    )
    namespace: Optional[str] = field(
        default=None,
        metadata={
            "name": "Namespace",
            "type": "Attribute",
        },
    )
    annotator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Annotator",
            "type": "Attribute",
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experimenter:\S+)|(Experimenter:\S+)",
        },
    )


@dataclass
class BinaryFile:
    """
    Describes a binary file.

    :ivar external:
    :ivar bin_data:
    :ivar file_name:
    :ivar size: Size of the uncompressed file. [unit:bytes]
    :ivar mimetype:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    external: Optional[External] = field(
        default=None,
        metadata={
            "name": "External",
            "type": "Element",
        },
    )
    bin_data: Optional[BinData] = field(
        default=None,
        metadata={
            "name": "BinData",
            "type": "Element",
        },
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Attribute",
            "required": True,
        },
    )
    size: Optional[int] = field(
        default=None,
        metadata={
            "name": "Size",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    mimetype: Optional[str] = field(
        default=None,
        metadata={
            "name": "MIMEType",
            "type": "Attribute",
        },
    )


@dataclass
class Dataset:
    """An element specifying a collection of images that are always processed
    together.

    Images can belong to more than one Dataset, and a Dataset may
    contain more than one Image. Images contain one or more DatasetRef
    elements to specify what datasets they belong to. Once a Dataset has
    been processed in any way, its collection of images cannot be
    altered. The ExperimenterRef and ExperimenterGroupRef elements
    specify the person and group this Dataset belongs to. Projects may
    contain one or more Datasets, and Datasets may belong to one or more
    Projects. This relationship is specified by listing DatasetRef
    elements within the Project element.

    :ivar description: A description for the dataset. [plain-text multi-
        line string]
    :ivar experimenter_ref:
    :ivar experimenter_group_ref:
    :ivar image_ref:
    :ivar annotation_ref:
    :ivar name: A name for the dataset that is suitable for presentation
        to the user.
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    experimenter_ref: Optional[ExperimenterRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
        },
    )
    experimenter_group_ref: Optional[ExperimenterGroupRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterGroupRef",
            "type": "Element",
        },
    )
    image_ref: list[ImageRef] = field(
        default_factory=list,
        metadata={
            "name": "ImageRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Dataset:\S+)|(Dataset:\S+)",
        },
    )


@dataclass
class Detector(ManufacturerSpec):
    """The type of detector used to capture the image.

    The Detector ID can be used as a reference within the Channel
    element in the Image element. The values stored in Detector
    represent the fixed values, variable values modified during the
    acquisition go in DetectorSettings Each attribute now has an
    indication of what type of detector it applies to. This is
    preparatory work for cleaning up and possibly splitting this object
    into sub-types.

    :ivar annotation_ref:
    :ivar gain: The Detector Gain for this detector, as a float.
        [units:none] {used:CCD,EMCCD,PMT}
    :ivar voltage: The Voltage of the detector (e.g. PMT voltage) as a
        float. {used:PMT} Units are set by VoltageUnit.
    :ivar voltage_unit: The units of the Voltage - default:volts[V].
    :ivar offset: The Detector Offset. [units:none] {used:CCD,EMCCD}
    :ivar zoom: The fixed Zoom for a detector. [units:none] {used:PMT}
    :ivar amplification_gain: Gain applied to the detector signal. This
        is the electronic gain (as apposed to the inherent gain) that is
        set for the detector. [units:none] {used:EMCCD#EMGain}
    :ivar id:
    :ivar type_value: The Type of detector. E.g. CCD, PMT, EMCCD etc.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Attribute",
        },
    )
    voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "Voltage",
            "type": "Attribute",
        },
    )
    voltage_unit: UnitsElectricPotential = field(
        default=UnitsElectricPotential.V,
        metadata={
            "name": "VoltageUnit",
            "type": "Attribute",
        },
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Attribute",
        },
    )
    zoom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Zoom",
            "type": "Attribute",
        },
    )
    amplification_gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "AmplificationGain",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Detector:\S+)|(Detector:\S+)",
        },
    )
    type_value: Optional[DetectorType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class DetectorSettings(Settings):
    """This holds the setting applied to a detector as well as a reference to the
    detector.

    The ID is the detector used in this case. The values stored in
    DetectorSettings represent the variable values, fixed values not
    modified during the acquisition go in Detector. Each attribute now
    has an indication of what type of detector it applies to. This is
    preparatory work for cleaning up and possibly splitting this object
    into sub-types.

    :ivar id:
    :ivar offset: The Offset of the detector. [units none]
        {used:CCD,EMCCD}
    :ivar gain: The Gain of the detector. [units:none]
        {used:CCD,EMCCD,PMT}
    :ivar voltage: The Voltage of the detector. {used:PMT} Units are set
        by VoltageUnit.
    :ivar voltage_unit: The units of the Voltage of the detector -
        default:volts[V]
    :ivar zoom: The Zoom or "Confocal Zoom" or "Scan Zoom" for a
        detector. [units:none] {used:PMT}
    :ivar read_out_rate: The speed at which the detector can count
        pixels.  {used:CCD,EMCCD} This is the bytes per second that can
        be read from the detector (like a baud rate). Units are set by
        ReadOutRateUnit.
    :ivar read_out_rate_unit: The units of the ReadOutRate -
        default:megahertz[Hz].
    :ivar binning: Represents the number of pixels that are combined to
        form larger pixels. {used:CCD,EMCCD}
    :ivar integration: This is the number of sequential frames that get
        averaged, to improve the signal-to-noise ratio. [units:none]
        {used:CCD,EMCCD}
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Detector:\S+)|(Detector:\S+)",
        },
    )
    offset: Optional[float] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Attribute",
        },
    )
    gain: Optional[float] = field(
        default=None,
        metadata={
            "name": "Gain",
            "type": "Attribute",
        },
    )
    voltage: Optional[float] = field(
        default=None,
        metadata={
            "name": "Voltage",
            "type": "Attribute",
        },
    )
    voltage_unit: UnitsElectricPotential = field(
        default=UnitsElectricPotential.V,
        metadata={
            "name": "VoltageUnit",
            "type": "Attribute",
        },
    )
    zoom: Optional[float] = field(
        default=None,
        metadata={
            "name": "Zoom",
            "type": "Attribute",
        },
    )
    read_out_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "ReadOutRate",
            "type": "Attribute",
        },
    )
    read_out_rate_unit: UnitsFrequency = field(
        default=UnitsFrequency.MHZ,
        metadata={
            "name": "ReadOutRateUnit",
            "type": "Attribute",
        },
    )
    binning: Optional[Binning] = field(
        default=None,
        metadata={
            "name": "Binning",
            "type": "Attribute",
        },
    )
    integration: Optional[int] = field(
        default=None,
        metadata={
            "name": "Integration",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class Dichroic(ManufacturerSpec):
    """
    The dichromatic beamsplitter or dichroic mirror used for this filter
    combination.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Dichroic:\S+)|(Dichroic:\S+)",
        },
    )


@dataclass
class Experimenter:
    """This element describes a person who performed an imaging experiment.

    This person may also be a user of the OME system, in which case the
    UserName element contains their login name. Experimenters may belong
    to one or more groups which are specified using one or more
    ExperimenterGroupRef elements.

    :ivar annotation_ref:
    :ivar id:
    :ivar first_name: First name, sometime called christian name or
        given name or forename. [plain text string]
    :ivar middle_name: Any other names. [plain text string]
    :ivar last_name: A person's last name sometimes called surname or
        family name. [plain text string]
    :ivar email: A person's email address. [valid email address as
        string]
    :ivar institution: A person's Institution The organizing structure
        that people belong to other than groups.  A university, or
        company, etc. We do not specify a department element, and do not
        mean for Institution to be used in this way. We simply wish to
        say XXX at YYY.  Where YYY has a better chance of being tied to
        a geographically fixed location and of being more recognizable
        than a group of experimenters. [plain text string]
    :ivar user_name: This is the username of the experimenter (in a
        'unix' or 'database' sense). [plain text string]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experimenter:\S+)|(Experimenter:\S+)",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Attribute",
        },
    )
    middle_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "MiddleName",
            "type": "Attribute",
        },
    )
    last_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Attribute",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Attribute",
        },
    )
    institution: Optional[str] = field(
        default=None,
        metadata={
            "name": "Institution",
            "type": "Attribute",
        },
    )
    user_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "UserName",
            "type": "Attribute",
        },
    )


@dataclass
class ExperimenterGroup:
    """The ExperimenterGroupID is required.

    Information should ideally be specified for at least one Leader as a
    contact for the group. The Leaders are themselves Experimenters.

    :ivar description: A description for the group. [plain-text multi-
        line string]
    :ivar experimenter_ref:
    :ivar leader:
    :ivar annotation_ref:
    :ivar name:
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    experimenter_ref: list[ExperimenterRef] = field(
        default_factory=list,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
        },
    )
    leader: list[Leader] = field(
        default_factory=list,
        metadata={
            "name": "Leader",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:ExperimenterGroup:\S+)|(ExperimenterGroup:\S+)",
        },
    )


@dataclass
class Filter(ManufacturerSpec):
    """A filter is either an excitation or emission filters. There should be one
    filter element specified per wavelength in the image. The channel number
    associated with a filter set is specified in Channel. It is based on the
    FilterSpec type, so has the required attributes Manufacturer, Model, and
    LotNumber. It may also contain a Type attribute which may be set to 'LongPass',
    'ShortPass', 'BandPass', 'MultiPass',

    'Dichroic', 'NeutralDensity', 'Tuneable' or 'Other'.
    It can be associated with an optional FilterWheel - Note: this is not the same as a FilterSet

    :ivar transmittance_range:
    :ivar annotation_ref:
    :ivar type_value:
    :ivar filter_wheel: A filter 'wheel' in OME can refer to any
        arrangement of filters in a filter holder of any shape. It
        could, for example, be a filter slider. [plain text string]
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    transmittance_range: Optional[TransmittanceRange] = field(
        default=None,
        metadata={
            "name": "TransmittanceRange",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    type_value: Optional[FilterType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    filter_wheel: Optional[str] = field(
        default=None,
        metadata={
            "name": "FilterWheel",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Filter:\S+)|(Filter:\S+)",
        },
    )


@dataclass
class FilterSet(ManufacturerSpec):
    """
    Filter set manufacturer specification.

    :ivar excitation_filter_ref: The Filters placed in the Excitation
        light path.
    :ivar dichroic_ref:
    :ivar emission_filter_ref: The Filters placed in the Emission light
        path.
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    excitation_filter_ref: list[FilterRef] = field(
        default_factory=list,
        metadata={
            "name": "ExcitationFilterRef",
            "type": "Element",
        },
    )
    dichroic_ref: Optional[DichroicRef] = field(
        default=None,
        metadata={
            "name": "DichroicRef",
            "type": "Element",
        },
    )
    emission_filter_ref: list[FilterRef] = field(
        default_factory=list,
        metadata={
            "name": "EmissionFilterRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:FilterSet:\S+)|(FilterSet:\S+)",
        },
    )


@dataclass
class Folder:
    """An element specifying a possibly heterogeneous collection of data.

    Folders may contain Folders so that data may be organized within a
    tree of Folders. Data may be in multiple Folders but a Folder may
    not be in more than one other Folder.

    :ivar description: A description for the folder. [plain-text multi-
        line string]
    :ivar folder_ref:
    :ivar image_ref:
    :ivar roiref:
    :ivar annotation_ref:
    :ivar id:
    :ivar name: A name for the folder that is suitable for presentation
        to the user.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    folder_ref: list[FolderRef] = field(
        default_factory=list,
        metadata={
            "name": "FolderRef",
            "type": "Element",
        },
    )
    image_ref: list[ImageRef] = field(
        default_factory=list,
        metadata={
            "name": "ImageRef",
            "type": "Element",
        },
    )
    roiref: list[Roiref] = field(
        default_factory=list,
        metadata={
            "name": "ROIRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Folder:\S+)|(Folder:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )


@dataclass
class LightPath:
    """
    A description of the light path.

    :ivar excitation_filter_ref: The Filters placed in the Excitation
        light path.
    :ivar dichroic_ref:
    :ivar emission_filter_ref: The Filters placed in the Emission light
        path.
    :ivar annotation_ref:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    excitation_filter_ref: list[FilterRef] = field(
        default_factory=list,
        metadata={
            "name": "ExcitationFilterRef",
            "type": "Element",
        },
    )
    dichroic_ref: Optional[DichroicRef] = field(
        default=None,
        metadata={
            "name": "DichroicRef",
            "type": "Element",
        },
    )
    emission_filter_ref: list[FilterRef] = field(
        default_factory=list,
        metadata={
            "name": "EmissionFilterRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )


@dataclass
class LightSource(ManufacturerSpec):
    """The lightsource for the instrument.

    An instrument may have several light sources. The type of
    lightsource is specified by one of the child-elements which are
    'Laser', 'Filament', 'Arc' or 'LightEmittingDiode'. Each of the
    light source types has its own Type attribute to further
    differentiate the light source (eg, Nd-YAG for Laser or Hg for Arc).

    :ivar annotation_ref:
    :ivar id: A LightSource ID must be specified for each light source,
        and the individual light sources can be referred to by their
        LightSource IDs (eg from Channel).
    :ivar power: The light-source power. Units are set by PowerUnit.
    :ivar power_unit: The units of the Power - default:milliwatts[mW].
    """

    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:LightSource:\S+)|(LightSource:\S+)",
        },
    )
    power: Optional[float] = field(
        default=None,
        metadata={
            "name": "Power",
            "type": "Attribute",
        },
    )
    power_unit: UnitsPower = field(
        default=UnitsPower.M_W_1,
        metadata={
            "name": "PowerUnit",
            "type": "Attribute",
        },
    )


@dataclass
class LightSourceSettings(Settings):
    """
    :ivar id:
    :ivar attenuation: The Attenuation of the light source [units:none]
        A fraction, as a value from 0.0 to 1.0.
    :ivar wavelength: The Wavelength of the light source. Units are set
        by WavelengthUnit.
    :ivar wavelength_unit: The units of the Wavelength of the light
        source - default:nanometres[nm]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:LightSource:\S+)|(LightSource:\S+)",
        },
    )
    attenuation: Optional[float] = field(
        default=None,
        metadata={
            "name": "Attenuation",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wavelength",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    wavelength_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "WavelengthUnit",
            "type": "Attribute",
        },
    )


@dataclass
class Objective(ManufacturerSpec):
    """A description of the microscope's objective lens.

    Required elements include the lens numerical aperture,
    and the magnification, both of which a floating
    point (real) numbers.
    The values are those that are fixed for a particular
    objective: either because it has been manufactured to
    this specification or the value has been measured on
    this particular objective.
    Correction: This is the type of correction coating applied to this lens.
    Immersion: This is the types of immersion medium the lens is designed to
    work with. It is not the same as 'Medium' in ObjectiveRef (a
    single type) as here Immersion can have compound values like 'Multi'.
    LensNA: The numerical aperture of the lens (as a float)
    NominalMagnification: The specified magnification e.g. x10
    CalibratedMagnification: The measured magnification e.g. x10.3
    WorkingDistance: WorkingDistance of the lens.

    :ivar annotation_ref:
    :ivar id:
    :ivar correction: The correction applied to the lens
    :ivar immersion: The immersion medium the lens is designed for
    :ivar lens_na: The numerical aperture of the lens expressed as a
        floating point (real) number. Expected range 0.02 - 1.5
        [units:none]
    :ivar nominal_magnification: The magnification of the lens as
        specified by the manufacturer - i.e. '60' is a 60X lens.
        [units:none] Note: The type of this has been changed from int to
        float to allow the specification of additional lenses e.g. 0.5X
        lens
    :ivar calibrated_magnification: The magnification of the lens as
        measured by a calibration process- i.e. '59.987' for a 60X lens.
        [units:none]
    :ivar working_distance: The working distance of the lens expressed
        as a floating point (real) number. Units are set by
        WorkingDistanceUnit.
    :ivar working_distance_unit: The units of the working distance -
        default:microns[µm].
    :ivar iris: Records whether or not the objective was fitted with an
        Iris. [flag]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Objective:\S+)|(Objective:\S+)",
        },
    )
    correction: Optional[ObjectiveCorrection] = field(
        default=None,
        metadata={
            "name": "Correction",
            "type": "Attribute",
        },
    )
    immersion: Optional[ObjectiveImmersion] = field(
        default=None,
        metadata={
            "name": "Immersion",
            "type": "Attribute",
        },
    )
    lens_na: Optional[float] = field(
        default=None,
        metadata={
            "name": "LensNA",
            "type": "Attribute",
        },
    )
    nominal_magnification: Optional[float] = field(
        default=None,
        metadata={
            "name": "NominalMagnification",
            "type": "Attribute",
        },
    )
    calibrated_magnification: Optional[float] = field(
        default=None,
        metadata={
            "name": "CalibratedMagnification",
            "type": "Attribute",
        },
    )
    working_distance: Optional[float] = field(
        default=None,
        metadata={
            "name": "WorkingDistance",
            "type": "Attribute",
        },
    )
    working_distance_unit: UnitsLength = field(
        default=UnitsLength.M_1,
        metadata={
            "name": "WorkingDistanceUnit",
            "type": "Attribute",
        },
    )
    iris: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Iris",
            "type": "Attribute",
        },
    )


@dataclass
class ObjectiveSettings(Settings):
    """This holds the setting applied to an objective as well as a reference to the
    objective.

    The ID is the objective used in this case.

    :ivar id:
    :ivar correction_collar: The CorrectionCollar is normally an
        adjustable ring on the objective. Each has an arbitrary scale on
        it so the values is unit-less. [units:none]
    :ivar medium:
    :ivar refractive_index: The RefractiveIndex is that of the immersion
        medium. This is a ratio so it also unit-less. [units:none]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Objective:\S+)|(Objective:\S+)",
        },
    )
    correction_collar: Optional[float] = field(
        default=None,
        metadata={
            "name": "CorrectionCollar",
            "type": "Attribute",
        },
    )
    medium: Optional[ObjectiveSettingsMedium] = field(
        default=None,
        metadata={
            "name": "Medium",
            "type": "Attribute",
        },
    )
    refractive_index: Optional[float] = field(
        default=None,
        metadata={
            "name": "RefractiveIndex",
            "type": "Attribute",
        },
    )


@dataclass
class Plane:
    """
    The Plane object holds microscope stage and image timing data for a given
    channel/z-section/timepoint.

    :ivar hash_sha1:
    :ivar annotation_ref:
    :ivar the_z: The Z-section this plane is for. [units:none] This is
        numbered from 0.
    :ivar the_t: The timepoint this plane is for. [units:none] This is
        numbered from 0.
    :ivar the_c: The channel this plane is for. [units:none] This is
        numbered from 0.
    :ivar delta_t: Time since the beginning of the experiment. Units are
        set by DeltaTUnit.
    :ivar delta_tunit: The units of the DeltaT - default:seconds[s].
    :ivar exposure_time: The length of the exposure. Units are set by
        ExposureTimeUnit.
    :ivar exposure_time_unit: The units of the ExposureTime -
        default:seconds[s].
    :ivar position_x: The X position of the stage. Units are set by
        PositionXUnit.
    :ivar position_xunit: The units of the X stage position -
        default:[reference frame].
    :ivar position_y: The Y position of the stage. Units are set by
        PositionYUnit.
    :ivar position_yunit: The units of the Y stage position -
        default:[reference frame].
    :ivar position_z: The Z position of the stage. Units are set by
        PositionZUnit.
    :ivar position_zunit: The units of the Z stage position -
        default:[reference frame].
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    hash_sha1: Optional[bytes] = field(
        default=None,
        metadata={
            "name": "HashSHA1",
            "type": "Element",
            "length": 20,
            "format": "base16",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    the_z: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheZ",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    the_t: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheT",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    the_c: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheC",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    delta_t: Optional[float] = field(
        default=None,
        metadata={
            "name": "DeltaT",
            "type": "Attribute",
        },
    )
    delta_tunit: UnitsTime = field(
        default=UnitsTime.S,
        metadata={
            "name": "DeltaTUnit",
            "type": "Attribute",
        },
    )
    exposure_time: Optional[float] = field(
        default=None,
        metadata={
            "name": "ExposureTime",
            "type": "Attribute",
        },
    )
    exposure_time_unit: UnitsTime = field(
        default=UnitsTime.S,
        metadata={
            "name": "ExposureTimeUnit",
            "type": "Attribute",
        },
    )
    position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "PositionX",
            "type": "Attribute",
        },
    )
    position_xunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "PositionXUnit",
            "type": "Attribute",
        },
    )
    position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "PositionY",
            "type": "Attribute",
        },
    )
    position_yunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "PositionYUnit",
            "type": "Attribute",
        },
    )
    position_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "PositionZ",
            "type": "Attribute",
        },
    )
    position_zunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "PositionZUnit",
            "type": "Attribute",
        },
    )


@dataclass
class PlateAcquisition:
    """PlateAcquisition is used to describe a single acquisition run for a plate.

    This object is used to record the set of images acquired in a single
    acquisition run. The Images for this run are linked to
    PlateAcquisition through WellSample.

    :ivar description: A description for the PlateAcquisition.
    :ivar well_sample_ref:
    :ivar annotation_ref:
    :ivar id:
    :ivar name:
    :ivar end_time: Time when the last image of this acquisition was
        collected
    :ivar start_time: Time when the first image of this acquisition was
        collected
    :ivar maximum_field_count: The maximum number of fields (well
        samples) in any well in this PlateAcquisition. This is only used
        to speed up user interaction by stopping the reading of every
        well sample.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    well_sample_ref: list[WellSampleRef] = field(
        default_factory=list,
        metadata={
            "name": "WellSampleRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:PlateAcquisition:\S+)|(PlateAcquisition:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Attribute",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Attribute",
        },
    )
    maximum_field_count: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumFieldCount",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )


@dataclass
class Project:
    """The Project ID is required. Datasets can be grouped into projects using a
    many-to-many relationship.

    A Dataset may belong to one or more Projects by including one or more ProjectRef elements which refer to Project IDs.
    Projects do not directly contain images - only by virtue of containing datasets, which themselves contain images.

    :ivar description: A description for the project. [plain-text multi-
        line string]
    :ivar experimenter_ref:
    :ivar experimenter_group_ref:
    :ivar dataset_ref:
    :ivar annotation_ref:
    :ivar name:
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    experimenter_ref: Optional[ExperimenterRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
        },
    )
    experimenter_group_ref: Optional[ExperimenterGroupRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterGroupRef",
            "type": "Element",
        },
    )
    dataset_ref: list[DatasetRef] = field(
        default_factory=list,
        metadata={
            "name": "DatasetRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Project:\S+)|(Project:\S+)",
        },
    )


@dataclass
class Reagent:
    """
    Reagent is used to describe a chemical or some other physical experimental
    parameter.

    :ivar description: A long description for the reagent.
    :ivar annotation_ref:
    :ivar id:
    :ivar name: A short name for the reagent
    :ivar reagent_identifier: This is a reference to an external (to
        OME) representation of the Reagent. It serves as a foreign key
        into an external database. - It is sometimes referred to as
        ExternalIdentifier.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Reagent:\S+)|(Reagent:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    reagent_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReagentIdentifier",
            "type": "Attribute",
        },
    )


@dataclass
class Shape:
    """The shape element contains a single specific ROI shape and links that to any
    channels, and a timepoint and a z-section.

    It also records any transform applied to the ROI shape.

    :ivar transform: This is a matrix used to transform the shape. The
        element has 6 xsd:float attributes. If the element is present
        then all 6 values must be included.
    :ivar annotation_ref:
    :ivar fill_color: The color of the fill - encoded as RGBA The value
        "-1" is #FFFFFFFF so solid white (it is a signed 32 bit value)
        NOTE: Prior to the 2012-06 schema the default value was
        incorrect and produced a transparent red not solid white.
    :ivar fill_rule:
    :ivar stroke_color: The color of the stroke  - encoded as RGBA The
        value "-1" is #FFFFFFFF so solid white (it is a signed 32 bit
        value) NOTE: Prior to the 2012-06 schema the default value was
        incorrect and produced a transparent red not solid white.
    :ivar stroke_width: The width of the stroke. Units are set by
        StrokeWidthUnit.
    :ivar stroke_width_unit: The units used for the stroke width.
    :ivar stroke_dash_array: e.g. "none", "10 20 30 10"
    :ivar text:
    :ivar font_family:
    :ivar font_size: Size of the font. Units are set by FontSizeUnit.
    :ivar font_size_unit: The units used for the font size.
    :ivar font_style:
    :ivar locked: Controls whether the shape is locked and read only,
        true is locked, false is editable.
    :ivar id:
    :ivar the_z: The z-section the ROI applies to. If not specified then
        the ROI applies to all the z-sections of the image. [units:none]
        This is numbered from 0.
    :ivar the_t: The timepoint the ROI applies to. If not specified then
        the ROI applies to all the timepoints of the image. [units:none]
        This is numbered from 0.
    :ivar the_c: The channel the ROI applies to. If not specified then
        the ROI applies to all the channels of the image. [units:none]
        This is numbered from 0.
    """

    transform: Optional[AffineTransform] = field(
        default=None,
        metadata={
            "name": "Transform",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
            "namespace": "http://www.openmicroscopy.org/Schemas/OME/2016-06",
        },
    )
    fill_color: Optional[int] = field(
        default=None,
        metadata={
            "name": "FillColor",
            "type": "Attribute",
        },
    )
    fill_rule: Optional[ShapeFillRule] = field(
        default=None,
        metadata={
            "name": "FillRule",
            "type": "Attribute",
        },
    )
    stroke_color: Optional[int] = field(
        default=None,
        metadata={
            "name": "StrokeColor",
            "type": "Attribute",
        },
    )
    stroke_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "StrokeWidth",
            "type": "Attribute",
        },
    )
    stroke_width_unit: UnitsLength = field(
        default=UnitsLength.PIXEL,
        metadata={
            "name": "StrokeWidthUnit",
            "type": "Attribute",
        },
    )
    stroke_dash_array: Optional[str] = field(
        default=None,
        metadata={
            "name": "StrokeDashArray",
            "type": "Attribute",
        },
    )
    text: Optional[str] = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
    font_family: Optional[ShapeFontFamily] = field(
        default=None,
        metadata={
            "name": "FontFamily",
            "type": "Attribute",
        },
    )
    font_size: Optional[int] = field(
        default=None,
        metadata={
            "name": "FontSize",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    font_size_unit: UnitsLength = field(
        default=UnitsLength.PT,
        metadata={
            "name": "FontSizeUnit",
            "type": "Attribute",
        },
    )
    font_style: Optional[ShapeFontStyle] = field(
        default=None,
        metadata={
            "name": "FontStyle",
            "type": "Attribute",
        },
    )
    locked: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Locked",
            "type": "Attribute",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Shape:\S+)|(Shape:\S+)",
        },
    )
    the_z: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheZ",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    the_t: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheT",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )
    the_c: Optional[int] = field(
        default=None,
        metadata={
            "name": "TheC",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )


@dataclass
class WellSample:
    """
    WellSample is an individual image that has been captured within a Well.

    :ivar image_ref: This is the main link to the core Image element
    :ivar id:
    :ivar position_x: The X position of the field (image) within the
        well relative to the well origin defined on the Plate. Units are
        set by PositionXUnit.
    :ivar position_xunit: The units of the position in X -
        default:reference frame.
    :ivar position_y: The Y position of the field (image) within the
        well relative to the well origin defined on the Plate. Units are
        set by PositionYUnit.
    :ivar position_yunit: The units of the position in Y -
        default:reference frame.
    :ivar timepoint: The time-point at which the image started to be
        collected
    :ivar index: This records the order of the well samples. Each index
        should be unique for a given plate but they do not have to be
        sequential, there may be gaps if part of the dataset is missing.
        In the user interface the displayed value of the index will be
        calculated modulo the number of PlateAcquisitions for the plate.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    image_ref: Optional[ImageRef] = field(
        default=None,
        metadata={
            "name": "ImageRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:WellSample:\S+)|(WellSample:\S+)",
        },
    )
    position_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "PositionX",
            "type": "Attribute",
        },
    )
    position_xunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "PositionXUnit",
            "type": "Attribute",
        },
    )
    position_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "PositionY",
            "type": "Attribute",
        },
    )
    position_yunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "PositionYUnit",
            "type": "Attribute",
        },
    )
    timepoint: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Timepoint",
            "type": "Attribute",
        },
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "name": "Index",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )


@dataclass
class Arc(LightSource):
    """The Arc element is used to describe various kinds of Arc lamps - Hg, Xe, HgXe.
    The Power of the Arc is now stored in the LightSource.

    :ivar type_value: The type of Arc lamp.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    type_value: Optional[ArcType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class BasicAnnotation(Annotation):
    """
    An abstract Basic Annotation from which some others are derived.
    """


@dataclass
class Channel:
    """There must be one per channel in the Image, even for a single-plane image.
    And information about how each of them was acquired is stored in the various
    optional *Ref elements.  Each Logical Channel is composed of one or more
    ChannelComponents.  For example, an entire spectrum in an FTIR experiment may
    be stored in a single Logical Channel with each discrete wavenumber of the
    spectrum.

    constituting a ChannelComponent of the FTIR Logical Channel.  An RGB image where the Red, Green and Blue components do not reflect discrete probes but are
    instead the output of a color camera would be treated similarly - one Logical channel with three ChannelComponents in this case.
    The total number of ChannelComponents for a set of pixels must equal SizeC.
    The IlluminationType attribute is a string enumeration which may be set to 'Transmitted', 'Epifluorescence', 'Oblique', or 'NonLinear'.
    The user interface logic for labeling a given channel for the user should use the first existing attribute in the following sequence:
    Name -&gt; Fluor -&gt; EmissionWavelength -&gt; ChannelComponent/Index.

    :ivar light_source_settings:
    :ivar detector_settings:
    :ivar filter_set_ref:
    :ivar annotation_ref:
    :ivar light_path:
    :ivar id:
    :ivar name: A name for the channel that is suitable for presentation
        to the user.
    :ivar samples_per_pixel: The number of samples the detector takes to
        form each pixel value. [units:none] Note: This is not the same
        as "Frame Averaging" - see Integration in DetectorSettings
    :ivar illumination_type: The method of illumination used to capture
        the channel.
    :ivar pinhole_size: The optional PinholeSize attribute allows
        specifying adjustable pin hole diameters for confocal
        microscopes. Units are set by PinholeSizeUnit.
    :ivar pinhole_size_unit: The units of the pin hole diameter for
        confocal microscopes - default:microns[µm].
    :ivar acquisition_mode: AcquisitionMode describes the type of
        microscopy performed for each channel
    :ivar contrast_method: ContrastMethod describes the technique used
        to achieve contrast for each channel
    :ivar excitation_wavelength: Wavelength of excitation for a
        particular channel. Units are set by ExcitationWavelengthUnit.
    :ivar excitation_wavelength_unit: The units of the wavelength of
        excitation - default:nanometres[nm].
    :ivar emission_wavelength: Wavelength of emission for a particular
        channel. Units are set by EmissionWavelengthUnit.
    :ivar emission_wavelength_unit: The units of the wavelength of
        emission - default:nanometres[nm].
    :ivar fluor: The Fluor attribute is used for fluorescence images.
        This is the name of the fluorophore used to produce this channel
        [plain text string]
    :ivar ndfilter: The NDfilter attribute is used to specify the
        combined effect of any neutral density filters used. The amount
        of light the filter transmits at a maximum [units:none] A
        fraction, as a value from 0.0 to 1.0. NOTE: This was formerly
        described as "units optical density expressed as a
        PercentFraction". This was how the field had been described in
        the schema from the beginning but all the use of it has been in
        the opposite direction, i.e. as a amount transmitted, not the
        amount blocked. This change has been made to make the model
        reflect this usage.
    :ivar pockel_cell_setting: The PockelCellSetting used for this
        channel. This is the amount the polarization of the beam is
        rotated by. [units:none]
    :ivar color: A color used to render this channel - encoded as RGBA
        The default value "-1" is #FFFFFFFF so solid white (it is a
        signed 32 bit value) NOTE: Prior to the 2012-06 schema the
        default value was incorrect and produced a transparent red not
        solid white.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    light_source_settings: Optional[LightSourceSettings] = field(
        default=None,
        metadata={
            "name": "LightSourceSettings",
            "type": "Element",
        },
    )
    detector_settings: Optional[DetectorSettings] = field(
        default=None,
        metadata={
            "name": "DetectorSettings",
            "type": "Element",
        },
    )
    filter_set_ref: Optional[FilterSetRef] = field(
        default=None,
        metadata={
            "name": "FilterSetRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    light_path: Optional[LightPath] = field(
        default=None,
        metadata={
            "name": "LightPath",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Channel:\S+)|(Channel:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    samples_per_pixel: Optional[int] = field(
        default=None,
        metadata={
            "name": "SamplesPerPixel",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    illumination_type: Optional[ChannelIlluminationType] = field(
        default=None,
        metadata={
            "name": "IlluminationType",
            "type": "Attribute",
        },
    )
    pinhole_size: Optional[float] = field(
        default=None,
        metadata={
            "name": "PinholeSize",
            "type": "Attribute",
        },
    )
    pinhole_size_unit: UnitsLength = field(
        default=UnitsLength.M_1,
        metadata={
            "name": "PinholeSizeUnit",
            "type": "Attribute",
        },
    )
    acquisition_mode: Optional[ChannelAcquisitionMode] = field(
        default=None,
        metadata={
            "name": "AcquisitionMode",
            "type": "Attribute",
        },
    )
    contrast_method: Optional[ChannelContrastMethod] = field(
        default=None,
        metadata={
            "name": "ContrastMethod",
            "type": "Attribute",
        },
    )
    excitation_wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "ExcitationWavelength",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    excitation_wavelength_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "ExcitationWavelengthUnit",
            "type": "Attribute",
        },
    )
    emission_wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "EmissionWavelength",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    emission_wavelength_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "EmissionWavelengthUnit",
            "type": "Attribute",
        },
    )
    fluor: Optional[str] = field(
        default=None,
        metadata={
            "name": "Fluor",
            "type": "Attribute",
        },
    )
    ndfilter: Optional[float] = field(
        default=None,
        metadata={
            "name": "NDFilter",
            "type": "Attribute",
        },
    )
    pockel_cell_setting: Optional[int] = field(
        default=None,
        metadata={
            "name": "PockelCellSetting",
            "type": "Attribute",
        },
    )
    color: int = field(
        default=-1,
        metadata={
            "name": "Color",
            "type": "Attribute",
        },
    )


@dataclass
class Ellipse(Shape):
    """A simple ellipse object.

    If rotation is required apply a transformation at the Shape level.

    :ivar x: The X coordinate of the center of the ellipse. [units
        pixels]
    :ivar y: The Y coordinate of the center of the ellipse. [units
        pixels]
    :ivar radius_x: The horizontal radius of the ellipse. [units pixels]
    :ivar radius_y: The vertical radius of the ellipse. [units pixels]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )
    radius_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "RadiusX",
            "type": "Attribute",
            "required": True,
        },
    )
    radius_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "RadiusY",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Filament(LightSource):
    """The Filament element is used to describe various kinds of filament bulbs
    such as Incadescent or Halogen.

    The Power of the Filament is now stored in the LightSource.

    :ivar type_value: The type of filament.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    type_value: Optional[FilamentType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )


@dataclass
class GenericExcitationSource(LightSource):
    """The GenericExcitationSource element is used to represent a source as a
    collection of key/value pairs, stored in a Map.

    The other lightsource objects should always be used in preference to
    this if possible.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    map: Optional[Map] = field(
        default=None,
        metadata={
            "name": "Map",
            "type": "Element",
        },
    )


@dataclass
class Label(Shape):
    """The text label.

    Any transformation should be applied at the shape level.

    :ivar x: This defines the X coordinate of the current text position
        of the first character in the string. [units pixels]
    :ivar y: This defines the Y coordinate of the current text position
        of the first character in the string. [units pixels]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Laser(LightSource):
    """Laser types are specified using two attributes - the Type and the LaserMedium.

    :ivar pump: The Laser element may contain a Pump sub-element which
        refers to a LightSource used as a laser pump.
    :ivar type_value: Type is the general category of laser.
    :ivar laser_medium: The Medium attribute specifies the actual lasing
        medium for a given laser type.
    :ivar wavelength: The Wavelength of the laser. Units are set by
        WavelengthUnit.
    :ivar wavelength_unit: The units of the Wavelength -
        default:nanometres[nm].
    :ivar frequency_multiplication: FrequencyMultiplication that may be
        specified. [units:none]
    :ivar tuneable: Whether or not the laser is Tuneable [flag]
    :ivar pulse: The Pulse mode of the laser.
    :ivar pockel_cell: If true the laser has a PockelCell to rotate the
        polarization of the beam. [flag]
    :ivar repetition_rate: The is the rate in Hz at which the laser
        pulses if the Pulse type is 'Repetitive'. hertz[Hz] Units are
        set by RepetitionRateUnit.
    :ivar repetition_rate_unit: The units of the RepetitionRate -
        default:hertz[Hz].
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    pump: Optional[Pump] = field(
        default=None,
        metadata={
            "name": "Pump",
            "type": "Element",
        },
    )
    type_value: Optional[LaserType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    laser_medium: Optional[LaserLaserMedium] = field(
        default=None,
        metadata={
            "name": "LaserMedium",
            "type": "Attribute",
        },
    )
    wavelength: Optional[float] = field(
        default=None,
        metadata={
            "name": "Wavelength",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    wavelength_unit: UnitsLength = field(
        default=UnitsLength.NM,
        metadata={
            "name": "WavelengthUnit",
            "type": "Attribute",
        },
    )
    frequency_multiplication: Optional[int] = field(
        default=None,
        metadata={
            "name": "FrequencyMultiplication",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    tuneable: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Tuneable",
            "type": "Attribute",
        },
    )
    pulse: Optional[LaserPulse] = field(
        default=None,
        metadata={
            "name": "Pulse",
            "type": "Attribute",
        },
    )
    pockel_cell: Optional[bool] = field(
        default=None,
        metadata={
            "name": "PockelCell",
            "type": "Attribute",
        },
    )
    repetition_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "RepetitionRate",
            "type": "Attribute",
        },
    )
    repetition_rate_unit: UnitsFrequency = field(
        default=UnitsFrequency.HZ,
        metadata={
            "name": "RepetitionRateUnit",
            "type": "Attribute",
        },
    )


@dataclass
class LightEmittingDiode(LightSource):
    """The LightEmittingDiode element is used to describe various kinds of LED
    lamps. As the LightEmittingDiode is inside a LightSource it already has
    available the values from ManufacturerSpec (Manufacturer, Model, SerialNumber,
    LotNumber) And the values from LightSource which includes Power in milliwatts
    We have looked at extending this element but have had a problem producing a
    generic solution.

    Possible attributes talked about adding include:
    Power in lumens - but this is complicated by multi-channel
    devices like CoolLED where each channel's power is different
    Wavelength Range - not a simple value so would require
    multiple attributes or a child element
    Angle of Projection - this would be further affected by the
    optics used for filtering the naked LED or that combine
    power from multiple devices
    These values are further affected if you over-drive the LED
    resulting in a more complex system
    Another issue is that LED's may not be used directly for
    illumination but as drivers for secondary emissions from doped
    fiber optics. This would require the fiber optics to be modeled.
    Thanks to Paul Goodwin of Applied Precision of information about
    this topic.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


@dataclass
class LightSourceGroup(LightSource):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


@dataclass
class Line(Shape):
    """
    A straight line defined by it's end points.

    :ivar x1: The X coordinate of the start of the line. [units pixels]
    :ivar y1: The Y coordinate of the start of the line. [units pixels]
    :ivar x2: The X coordinate of the end of the line. [units pixels]
    :ivar y2: The Y coordinate of the end of the line. [units pixels]
    :ivar marker_start:
    :ivar marker_end:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    x1: Optional[float] = field(
        default=None,
        metadata={
            "name": "X1",
            "type": "Attribute",
            "required": True,
        },
    )
    y1: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y1",
            "type": "Attribute",
            "required": True,
        },
    )
    x2: Optional[float] = field(
        default=None,
        metadata={
            "name": "X2",
            "type": "Attribute",
            "required": True,
        },
    )
    y2: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y2",
            "type": "Attribute",
            "required": True,
        },
    )
    marker_start: Optional[Marker] = field(
        default=None,
        metadata={
            "name": "MarkerStart",
            "type": "Attribute",
        },
    )
    marker_end: Optional[Marker] = field(
        default=None,
        metadata={
            "name": "MarkerEnd",
            "type": "Attribute",
        },
    )


@dataclass
class ListAnnotation(Annotation):
    """This annotation is a grouping object.

    It uses the sequence of annotation refs from the base Annotation to
    form the list.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


@dataclass
class MapAnnotation(Annotation):
    """An map annotation.

    The contents of this is a list of key/value pairs.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[Map] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Mask(Shape):
    """The Mask ROI shape is a link to a BinData object that is a BIT mask drawn on
    top of the image as an ROI.

    It is applied at the same scale, pixel to pixel, as the Image the
    ROI is applied to, unless a transform is applied at the shape level.

    :ivar bin_data:
    :ivar x: The X coordinate of the left side of the image. [units
        pixels]
    :ivar y: The Y coordinate of the top side of the image. [units
        pixels]
    :ivar width: The width of the mask. [units pixels]
    :ivar height: The height of the mask. [units pixels]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    bin_data: Optional[BinData] = field(
        default=None,
        metadata={
            "name": "BinData",
            "type": "Element",
            "required": True,
        },
    )
    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Attribute",
            "required": True,
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class MicrobeamManipulation:
    """Defines a microbeam operation type and the region of the image it was
    applied to.

    The LightSourceRef element is a reference to a LightSource specified
    in the Instrument element which was used for a technique other than
    illumination for the purpose of imaging. For example, a laser used
    for photobleaching.

    :ivar description: A description for the Microbeam Manipulation.
        [plain-text multi-line string]
    :ivar roiref:
    :ivar experimenter_ref:
    :ivar light_source_settings:
    :ivar id:
    :ivar type_value: The type of manipulation performed.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    roiref: list[Roiref] = field(
        default_factory=list,
        metadata={
            "name": "ROIRef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    experimenter_ref: Optional[ExperimenterRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
            "required": True,
        },
    )
    light_source_settings: list[LightSourceSettings] = field(
        default_factory=list,
        metadata={
            "name": "LightSourceSettings",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:MicrobeamManipulation:\S+)|(MicrobeamManipulation:\S+)",
        },
    )
    type_value: list[MicrobeamManipulationValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )


@dataclass
class Point(Shape):
    """
    :ivar x: The X coordinate of the point. [units pixels]
    :ivar y: The Y coordinate of the point. [units pixels]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Polygon(Shape):
    """The Polygon defines closed shapes formed of straight lines.

    Note: Polygon uses counterclockwise winding (this is the
    default OpenGL behavior)

    :ivar points: The points of the Polygon are defined as a list of
        comma separated x,y coordinates seperated by spaces like "x1,y1
        x2,y2 x3,y3" e.g. "0,0 1,2 3,5"
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    points: Optional[str] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Polyline(Shape):
    """The Polyline defines open shapes formed of straight lines.

    Note: Polyline uses counterclockwise winding (this is the
    default OpenGL behavior)

    :ivar points: The points of the polyline are defined as a list of
        comma separated x,y coordinates seperated by spaces like "x1,y1
        x2,y2 x3,y3" e.g. "0,0 1,2 3,5"
    :ivar marker_start:
    :ivar marker_end:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    points: Optional[str] = field(
        default=None,
        metadata={
            "name": "Points",
            "type": "Attribute",
            "required": True,
        },
    )
    marker_start: Optional[Marker] = field(
        default=None,
        metadata={
            "name": "MarkerStart",
            "type": "Attribute",
        },
    )
    marker_end: Optional[Marker] = field(
        default=None,
        metadata={
            "name": "MarkerEnd",
            "type": "Attribute",
        },
    )


@dataclass
class Rectangle(Shape):
    """A simple rectangle object.

    If rotation is required apply a transformation at the Shape level.

    :ivar x: The X value of the left edge or the rectangle. [units
        pixels]
    :ivar y: The y value of the top edge or the rectangle. [units
        pixels]
    :ivar width: The width of the rectangle. [units pixels]
    :ivar height: The height of the rectangle. [units pixels]
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    x: Optional[float] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Attribute",
            "required": True,
        },
    )
    y: Optional[float] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Attribute",
            "required": True,
        },
    )
    width: Optional[float] = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Attribute",
            "required": True,
        },
    )
    height: Optional[float] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Screen:
    """The Screen element is a grouping for Plates.

    The required attribute is the Screen's Name and ID - both must be unique within the document.
    The Screen element may contain an ExternalRef attribute that refers to an external database.
    A description of the screen may be specified in the Description element.
    Screens may contain overlapping sets of Plates i.e.      Screens and Plates have a many-to-many relationship.
    Plates contain one or more ScreenRef elements to specify what screens they belong to.

    :ivar description: A description for the screen.
    :ivar reagent:
    :ivar plate_ref: The PlateRef element is a reference to a Plate
        element. Screen elements may have one or more PlateRef elements
        to define the plates that are part of the screen. Plates may
        belong to more than one screen.
    :ivar annotation_ref:
    :ivar id:
    :ivar name:
    :ivar protocol_identifier: A pointer to an externally defined
        protocol, usually in a screening database.
    :ivar protocol_description: A description of the screen protocol;
        may contain very detailed information to reproduce some of that
        found in a screening database.
    :ivar reagent_set_description: A description of the set of reagents;
        may contain very detailed information to reproduce some of that
        information found in a screening database.
    :ivar reagent_set_identifier: A pointer to an externally defined set
        of reagents, usually in a screening database/automation
        database.
    :ivar type_value: A human readable identifier for the screen type;
        e.g. RNAi, cDNA, SiRNA, etc. This string is likely to become an
        enumeration in future releases.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    reagent: list[Reagent] = field(
        default_factory=list,
        metadata={
            "name": "Reagent",
            "type": "Element",
        },
    )
    plate_ref: list["Screen.PlateRef"] = field(
        default_factory=list,
        metadata={
            "name": "PlateRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Screen:\S+)|(Screen:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    protocol_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProtocolIdentifier",
            "type": "Attribute",
        },
    )
    protocol_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ProtocolDescription",
            "type": "Attribute",
        },
    )
    reagent_set_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReagentSetDescription",
            "type": "Attribute",
        },
    )
    reagent_set_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ReagentSetIdentifier",
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )

    @dataclass
    class PlateRef(Reference):
        id: Optional[str] = field(
            default=None,
            metadata={
                "name": "ID",
                "type": "Attribute",
                "required": True,
                "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Plate:\S+)|(Plate:\S+)",
            },
        )


@dataclass
class ShapeGroup(Shape):
    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"


@dataclass
class TextAnnotation(Annotation):
    """
    An abstract Text Annotation from which some others are derived.
    """


@dataclass
class TypeAnnotation(Annotation):
    """
    An abstract Type Annotation from which some others are derived.
    """


@dataclass
class Well:
    """A Well is a component of the Well/Plate/Screen construct to describe
    screening applications.

    A Well has a number of WellSample elements that link to the Images
    collected in this well. The ReagentRef links any Reagents that were
    used in this Well. A well is part of only one Plate. The origin for
    the row and column identifiers is the top left corner of the plate
    starting at zero. i.e The top left well of a plate is index (0,0)

    :ivar well_sample:
    :ivar reagent_ref:
    :ivar annotation_ref:
    :ivar id:
    :ivar column: This is the column index of the well, the origin is
        the top left corner of the plate with the first column of cells
        being column zero. i.e top left is (0,0) The combination of Row,
        Column has to be unique for each well in a plate.
    :ivar row: This is the row index of the well, the origin is the top
        left corner of the plate with the first row of wells being row
        zero. i.e top left is (0,0) The combination of Row, Column has
        to be unique for each well in a plate.
    :ivar external_description: A description of the externally defined
        identifier for this plate.
    :ivar external_identifier: The ExternalIdentifier attribute may
        contain a reference to an external database.
    :ivar type_value: A human readable identifier for the screening
        status. e.g. empty, positive control, negative control, control,
        experimental, etc.
    :ivar color: A marker color used to highlight the well - encoded as
        RGBA The default value "-1" is #FFFFFFFF so solid white (it is a
        signed 32 bit value) NOTE: Prior to the 2012-06 schema the
        default value was incorrect and produced a transparent red not
        solid white.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    well_sample: list[WellSample] = field(
        default_factory=list,
        metadata={
            "name": "WellSample",
            "type": "Element",
        },
    )
    reagent_ref: Optional[ReagentRef] = field(
        default=None,
        metadata={
            "name": "ReagentRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Well:\S+)|(Well:\S+)",
        },
    )
    column: Optional[int] = field(
        default=None,
        metadata={
            "name": "Column",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    row: Optional[int] = field(
        default=None,
        metadata={
            "name": "Row",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )
    external_description: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalDescription",
            "type": "Attribute",
        },
    )
    external_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Attribute",
        },
    )
    type_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    color: int = field(
        default=-1,
        metadata={
            "name": "Color",
            "type": "Attribute",
        },
    )


@dataclass
class BooleanAnnotation(BasicAnnotation):
    """
    A simple boolean annotation of type xsd:boolean.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class CommentAnnotation(TextAnnotation):
    """
    A simple comment annotation.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Experiment:
    """This element describes the type of experiment.

    The required Type attribute must contain one or more entries from the following list:
    FP FRET Time-lapse 4-D+ Screen Immunocytochemistry FISH Electrophysiology  Ion-Imaging Colocalization PGI/Documentation
    FRAP Photoablation Optical-Trapping Photoactivation Fluorescence-Lifetime Spectral-Imaging Other
    FP refers to fluorescent proteins, PGI/Documentation is not a 'data' image.
    The optional Description element may contain free text to further describe the experiment.

    :ivar description: A description for the experiment. [plain-text
        multi-line string]
    :ivar experimenter_ref: This is a link to the Experimenter who
        conducted the experiment
    :ivar microbeam_manipulation:
    :ivar type_value: A term to describe the type of experiment.
    :ivar id:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    experimenter_ref: Optional[ExperimenterRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
        },
    )
    microbeam_manipulation: list[MicrobeamManipulation] = field(
        default_factory=list,
        metadata={
            "name": "MicrobeamManipulation",
            "type": "Element",
        },
    )
    type_value: list[ExperimentValue] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "tokens": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Experiment:\S+)|(Experiment:\S+)",
        },
    )


@dataclass
class FileAnnotation(TypeAnnotation):
    """
    A file object annotation.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    binary_file: Optional[BinaryFile] = field(
        default=None,
        metadata={
            "name": "BinaryFile",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Instrument:
    """This element describes the instrument used to capture the Image.

    It is primarily a container for manufacturer's model and catalog
    numbers for the Microscope, LightSource, Detector, Objective and
    Filters components. The Objective element contains the additional
    elements LensNA and Magnification. The Filters element can be
    composed either of separate excitation, emission filters and a
    dichroic mirror or a single filter set. Within the Image itself, a
    reference is made to this one Filter element. There may be multiple
    light sources, detectors, objectives and filters on a microscope.
    Each of these has their own ID attribute, which can be referred to
    from Channel. It is understood that the light path configuration can
    be different for each channel, but cannot be different for each
    timepoint or each plane of an XYZ stack.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    microscope: Optional[Microscope] = field(
        default=None,
        metadata={
            "name": "Microscope",
            "type": "Element",
        },
    )
    generic_excitation_source: list[GenericExcitationSource] = field(
        default_factory=list,
        metadata={
            "name": "GenericExcitationSource",
            "type": "Element",
        },
    )
    light_emitting_diode: list[LightEmittingDiode] = field(
        default_factory=list,
        metadata={
            "name": "LightEmittingDiode",
            "type": "Element",
        },
    )
    filament: list[Filament] = field(
        default_factory=list,
        metadata={
            "name": "Filament",
            "type": "Element",
        },
    )
    arc: list[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
        },
    )
    laser: list[Laser] = field(
        default_factory=list,
        metadata={
            "name": "Laser",
            "type": "Element",
        },
    )
    detector: list[Detector] = field(
        default_factory=list,
        metadata={
            "name": "Detector",
            "type": "Element",
        },
    )
    objective: list[Objective] = field(
        default_factory=list,
        metadata={
            "name": "Objective",
            "type": "Element",
        },
    )
    filter_set: list[FilterSet] = field(
        default_factory=list,
        metadata={
            "name": "FilterSet",
            "type": "Element",
        },
    )
    filter: list[Filter] = field(
        default_factory=list,
        metadata={
            "name": "Filter",
            "type": "Element",
        },
    )
    dichroic: list[Dichroic] = field(
        default_factory=list,
        metadata={
            "name": "Dichroic",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Instrument:\S+)|(Instrument:\S+)",
        },
    )


@dataclass
class NumericAnnotation(BasicAnnotation):
    """
    An abstract Numeric Annotation from which some others are derived.
    """


@dataclass
class Pixels:
    """Pixels is going to be removed in the future, but it is still required.

    This is just notice that the contents of Pixels will be moved up to
    Image in a future release. This is because there has only been 1
    Pixels object in each Image for some time. The concept of multiple
    Pixels sets for one Image failed to take off. It is therefore
    redundant. The Image will be unreadable if any of the required Pixel
    attributes are missing. The Pixels themselves can be stored within
    the OME-XML compressed by plane, and encoded in Base64. Or the
    Pixels may be stored in TIFF format. The Pixels element should
    contain a list of BinData or TiffData, each containing a single
    plane of pixels. These Pixels elements, when read in document order,
    must produce a 5-D pixel array of the size specified in this
    element, and in the dimension order specified by 'DimensionOrder'.
    All of the values in the Pixels object when present should match the
    same value stored in any associated TIFF format (e.g. SizeX should
    be the same). Where there is a mismatch our readers will take the
    value from the TIFF structure as overriding the value in the OME-
    XML. This is simply a pragmatic decision as it increases the
    likelihood of reading data from a slightly incorrect file.

    :ivar channel:
    :ivar bin_data:
    :ivar tiff_data:
    :ivar metadata_only:
    :ivar plane:
    :ivar id:
    :ivar dimension_order: The order in which the individual planes of
        data are interleaved.
    :ivar type_value: The variable type used to represent each pixel in
        the image.
    :ivar significant_bits: The number of bits within the type storing
        each pixel that are significant. e.g. you can store 12 bit data
        within a 16 bit type. This does not reduce the storage
        requirements but can be a useful indicator when processing or
        viewing the image data.
    :ivar interleaved: How the channels are arranged within the data
        block: true if channels are stored RGBRGBRGB...; false if
        channels are stored RRR...GGG...BBB...
    :ivar big_endian: This is true if the pixels data was written in
        BigEndian order. If this value is present it should match the
        value used in BinData or TiffData. If it does not a reader
        should honour the value used in the BinData or TiffData. This
        values is useful for MetadataOnly files and is to allow for
        future storage solutions.
    :ivar size_x: Dimensional size of pixel data array [units:none]
    :ivar size_y: Dimensional size of pixel data array [units:none]
    :ivar size_z: Dimensional size of pixel data array [units:none]
    :ivar size_c: Dimensional size of pixel data array [units:none]
    :ivar size_t: Dimensional size of pixel data array [units:none]
    :ivar physical_size_x: Physical size of a pixel. Units are set by
        PhysicalSizeXUnit.
    :ivar physical_size_xunit: The units of the physical size of a pixel
        - default:microns[µm].
    :ivar physical_size_y: Physical size of a pixel. Units are set by
        PhysicalSizeYUnit.
    :ivar physical_size_yunit: The units of the physical size of a pixel
        - default:microns[µm].
    :ivar physical_size_z: Physical size of a pixel. Units are set by
        PhysicalSizeZUnit.
    :ivar physical_size_zunit: The units of the physical size of a pixel
        - default:microns[µm].
    :ivar time_increment: TimeIncrement is used for time series that
        have a global timing specification instead of per-timepoint
        timing info. For example in a video stream. Units are set by
        TimeIncrementUnit.
    :ivar time_increment_unit: The units of the TimeIncrement -
        default:seconds[s].
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    channel: list[Channel] = field(
        default_factory=list,
        metadata={
            "name": "Channel",
            "type": "Element",
        },
    )
    bin_data: list[BinData] = field(
        default_factory=list,
        metadata={
            "name": "BinData",
            "type": "Element",
        },
    )
    tiff_data: list[TiffData] = field(
        default_factory=list,
        metadata={
            "name": "TiffData",
            "type": "Element",
        },
    )
    metadata_only: Optional[MetadataOnly] = field(
        default=None,
        metadata={
            "name": "MetadataOnly",
            "type": "Element",
        },
    )
    plane: list[Plane] = field(
        default_factory=list,
        metadata={
            "name": "Plane",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Pixels:\S+)|(Pixels:\S+)",
        },
    )
    dimension_order: Optional[PixelsDimensionOrder] = field(
        default=None,
        metadata={
            "name": "DimensionOrder",
            "type": "Attribute",
            "required": True,
        },
    )
    type_value: Optional[PixelType] = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    significant_bits: Optional[int] = field(
        default=None,
        metadata={
            "name": "SignificantBits",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    interleaved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Interleaved",
            "type": "Attribute",
        },
    )
    big_endian: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BigEndian",
            "type": "Attribute",
        },
    )
    size_x: Optional[int] = field(
        default=None,
        metadata={
            "name": "SizeX",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )
    size_y: Optional[int] = field(
        default=None,
        metadata={
            "name": "SizeY",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )
    size_z: Optional[int] = field(
        default=None,
        metadata={
            "name": "SizeZ",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )
    size_c: Optional[int] = field(
        default=None,
        metadata={
            "name": "SizeC",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )
    size_t: Optional[int] = field(
        default=None,
        metadata={
            "name": "SizeT",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
        },
    )
    physical_size_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "PhysicalSizeX",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    physical_size_xunit: UnitsLength = field(
        default=UnitsLength.M_1,
        metadata={
            "name": "PhysicalSizeXUnit",
            "type": "Attribute",
        },
    )
    physical_size_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "PhysicalSizeY",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    physical_size_yunit: UnitsLength = field(
        default=UnitsLength.M_1,
        metadata={
            "name": "PhysicalSizeYUnit",
            "type": "Attribute",
        },
    )
    physical_size_z: Optional[float] = field(
        default=None,
        metadata={
            "name": "PhysicalSizeZ",
            "type": "Attribute",
            "min_exclusive": 0.0,
        },
    )
    physical_size_zunit: UnitsLength = field(
        default=UnitsLength.M_1,
        metadata={
            "name": "PhysicalSizeZUnit",
            "type": "Attribute",
        },
    )
    time_increment: Optional[float] = field(
        default=None,
        metadata={
            "name": "TimeIncrement",
            "type": "Attribute",
        },
    )
    time_increment_unit: UnitsTime = field(
        default=UnitsTime.S,
        metadata={
            "name": "TimeIncrementUnit",
            "type": "Attribute",
        },
    )


@dataclass
class Plate:
    """This element identifies microtiter plates within a screen.

    A plate can belong to more than one screen. The Screen(s) that a
    plate belongs to are specified by the ScreenRef element. The Plate
    ID and Name attributes are required. The Wells in a plate are
    numbers from the top-left corner in a grid starting at zero. i.e.
    The top-left well of a plate is index (0,0)

    :ivar description: A description for the plate.
    :ivar well:
    :ivar annotation_ref:
    :ivar plate_acquisition:
    :ivar id:
    :ivar name: The Name identifies the plate to the user. It is used
        much like the ID, and so must be unique within the document. If
        a plate name is not available when one is needed it will be
        constructed in the following order: 1. If name is available use
        it. 2. If not use "Start time - End time" (NOTE: Not a
        subtraction! A string representation of the two times separated
        by a dash.) 3. If these times are not available use the Plate
        ID.
    :ivar status: A textual annotation of the current state of the plate
        with respect to the experiment work-flow; e.g. 1. Seed cell:
        done; 2. Transfection: done;      3. Gel doc: todo.
    :ivar external_identifier: The ExternalIdentifier attribute may
        contain a reference to an external database.
    :ivar column_naming_convention: The ColumnNamingConvention
    :ivar row_naming_convention: The RowNamingConvention
    :ivar well_origin_x: This defines the X position to use for the
        origin of the fields (individual images) taken in a well. It is
        used with the X in the WellSample to display the fields in the
        correct position relative to each other. Each Well in the plate
        has the same well origin. Units are set by WellOriginXUnit. In
        the OMERO clients by convention we display the WellOrigin in the
        center of the view.
    :ivar well_origin_xunit: The units of the well origin in X -
        default:reference frame.
    :ivar well_origin_y: This defines the Y position to use for the
        origin of the fields (individual images) taken in a well. It is
        used with the Y in the WellSample to display the fields in the
        correct position relative to each other. Each Well in the plate
        has the same well origin.  Units are set by WellOriginYUnit. In
        the OMERO clients by convention we display the WellOrigin in the
        center of the view.
    :ivar well_origin_yunit: The units of the well origin in Y -
        default:reference frame.
    :ivar rows: The number of rows in the plate
    :ivar columns: The number of columns in the plate
    :ivar field_index: The index of the WellSample to display as the
        default Field
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    well: list[Well] = field(
        default_factory=list,
        metadata={
            "name": "Well",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    plate_acquisition: list[PlateAcquisition] = field(
        default_factory=list,
        metadata={
            "name": "PlateAcquisition",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Plate:\S+)|(Plate:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    status: Optional[str] = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    external_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Attribute",
        },
    )
    column_naming_convention: Optional[NamingConvention] = field(
        default=None,
        metadata={
            "name": "ColumnNamingConvention",
            "type": "Attribute",
        },
    )
    row_naming_convention: Optional[NamingConvention] = field(
        default=None,
        metadata={
            "name": "RowNamingConvention",
            "type": "Attribute",
        },
    )
    well_origin_x: Optional[float] = field(
        default=None,
        metadata={
            "name": "WellOriginX",
            "type": "Attribute",
        },
    )
    well_origin_xunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "WellOriginXUnit",
            "type": "Attribute",
        },
    )
    well_origin_y: Optional[float] = field(
        default=None,
        metadata={
            "name": "WellOriginY",
            "type": "Attribute",
        },
    )
    well_origin_yunit: UnitsLength = field(
        default=UnitsLength.REFERENCE_FRAME,
        metadata={
            "name": "WellOriginYUnit",
            "type": "Attribute",
        },
    )
    rows: Optional[int] = field(
        default=None,
        metadata={
            "name": "Rows",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "name": "Columns",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    field_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "FieldIndex",
            "type": "Attribute",
            "min_inclusive": 0,
        },
    )


@dataclass
class Roi:
    """A four dimensional 'Region of Interest'.

    If they are not used, and the Image has more than one plane, the
    entire set of planes is assumed to be included in the ROI. Multiple
    ROIs may be specified.

    :ivar union:
    :ivar annotation_ref:
    :ivar description: A description for the ROI. [plain-text multi-line
        string]
    :ivar id:
    :ivar name: The Name identifies the ROI to the user. [plain-text
        string]
    """

    class Meta:
        name = "ROI"
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    union: Optional["Roi.UnionType"] = field(
        default=None,
        metadata={
            "name": "Union",
            "type": "Element",
            "required": True,
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:\S+)|(\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )

    @dataclass
    class UnionType:
        label: list[Label] = field(
            default_factory=list,
            metadata={
                "name": "Label",
                "type": "Element",
            },
        )
        polygon: list[Polygon] = field(
            default_factory=list,
            metadata={
                "name": "Polygon",
                "type": "Element",
            },
        )
        polyline: list[Polyline] = field(
            default_factory=list,
            metadata={
                "name": "Polyline",
                "type": "Element",
            },
        )
        line: list[Line] = field(
            default_factory=list,
            metadata={
                "name": "Line",
                "type": "Element",
            },
        )
        ellipse: list[Ellipse] = field(
            default_factory=list,
            metadata={
                "name": "Ellipse",
                "type": "Element",
            },
        )
        point: list[Point] = field(
            default_factory=list,
            metadata={
                "name": "Point",
                "type": "Element",
            },
        )
        mask: list[Mask] = field(
            default_factory=list,
            metadata={
                "name": "Mask",
                "type": "Element",
            },
        )
        rectangle: list[Rectangle] = field(
            default_factory=list,
            metadata={
                "name": "Rectangle",
                "type": "Element",
            },
        )


@dataclass
class TagAnnotation(TextAnnotation):
    """
    A tag annotation (represents a tag or a tagset)
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TermAnnotation(BasicAnnotation):
    """
    A ontology term annotation.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[str] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class TimestampAnnotation(BasicAnnotation):
    """
    A date/time annotation of type xsd:dateTime.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Xmlannotation(TextAnnotation):
    """An general xml annotation.

    The contents of this is not processed as OME XML but should still be
    well-formed XML.
    """

    class Meta:
        name = "XMLAnnotation"
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional["Xmlannotation.Value"] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )

    @dataclass
    class Value:
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )


@dataclass
class DoubleAnnotation(NumericAnnotation):
    """
    A simple numerical annotation of type xsd:double.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[float] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class Image:
    """This element describes the actual image and its meta-data.

    The elements that are references (ending in Ref or Settings) refer
    to elements defined outside of the Image element. Ref elements are
    simple links, while Settings elements are links with additional
    values. If any of the required Image attributes or elements are
    missing, its guaranteed to be an invalid document. The required
    attributes and elements are ID and Pixels. ExperimenterRef is
    required for all Images with well formed LSIDs. ImageType is a
    vendor-specific designation of the type of image this is. Examples
    of ImageType include 'STK', 'SoftWorx', etc. The Name attributes are
    in all cases the name of the element instance. In this case, the
    name of the image, not necessarily the filename. Physical size of
    pixels are microns[µm].

    :ivar acquisition_date: The acquisition date of the Image. The
        element contains an xsd:dateTime string based on the ISO 8601
        format (i.e. 1988-04-07T18:39:09.359) YYYY-MM-DDTHH:mm:SS.sssZ Y
        - Year M - Month D - Day H - Hour m - minutes S - Seconds s -
        sub-seconds (optional) Z - Zone (optional) +HH:mm or -HH:mm or Z
        for UTC Note: xsd:dataTime supports a very wide date range with
        unlimited precision. The full date range and precision are not
        typically supported by platform- and language-specific
        libraries. Where the supported time precision is less than the
        precision used by the xsd:dateTime timestamp there will be loss
        of precision; this will typically occur via direct truncation or
        (less commonly) rounding. The year value can be large and/or
        negative. Any value covering the current or last century should
        be correctly processed, but some systems cannot process earlier
        dates. The sub-second value is defined as an unlimited number of
        digits after the decimal point. In Java a minimum of millisecond
        precision is guaranteed. In C++ microsecond precision is
        guaranteed, with nanosecond precision being available on some
        platforms. Time zones are supported, eg
        '2013-10-24T11:52:33+01:00' for Paris, but in most cases it will
        be converted to UTC when the timestamp is written.
    :ivar experimenter_ref:
    :ivar description: A description for the image. [plain-text multi-
        line string]
    :ivar experiment_ref:
    :ivar experimenter_group_ref:
    :ivar instrument_ref:
    :ivar objective_settings:
    :ivar imaging_environment:
    :ivar stage_label:
    :ivar pixels:
    :ivar roiref:
    :ivar microbeam_manipulation_ref:
    :ivar annotation_ref:
    :ivar id:
    :ivar name:
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    acquisition_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "AcquisitionDate",
            "type": "Element",
        },
    )
    experimenter_ref: Optional[ExperimenterRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterRef",
            "type": "Element",
        },
    )
    description: Optional[str] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "white_space": "preserve",
        },
    )
    experiment_ref: Optional[ExperimentRef] = field(
        default=None,
        metadata={
            "name": "ExperimentRef",
            "type": "Element",
        },
    )
    experimenter_group_ref: Optional[ExperimenterGroupRef] = field(
        default=None,
        metadata={
            "name": "ExperimenterGroupRef",
            "type": "Element",
        },
    )
    instrument_ref: Optional[InstrumentRef] = field(
        default=None,
        metadata={
            "name": "InstrumentRef",
            "type": "Element",
        },
    )
    objective_settings: Optional[ObjectiveSettings] = field(
        default=None,
        metadata={
            "name": "ObjectiveSettings",
            "type": "Element",
        },
    )
    imaging_environment: Optional[ImagingEnvironment] = field(
        default=None,
        metadata={
            "name": "ImagingEnvironment",
            "type": "Element",
        },
    )
    stage_label: Optional[StageLabel] = field(
        default=None,
        metadata={
            "name": "StageLabel",
            "type": "Element",
        },
    )
    pixels: Optional[Pixels] = field(
        default=None,
        metadata={
            "name": "Pixels",
            "type": "Element",
            "required": True,
        },
    )
    roiref: list[Roiref] = field(
        default_factory=list,
        metadata={
            "name": "ROIRef",
            "type": "Element",
        },
    )
    microbeam_manipulation_ref: list[MicrobeamManipulationRef] = field(
        default_factory=list,
        metadata={
            "name": "MicrobeamManipulationRef",
            "type": "Element",
        },
    )
    annotation_ref: list[AnnotationRef] = field(
        default_factory=list,
        metadata={
            "name": "AnnotationRef",
            "type": "Element",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
            "required": True,
            "pattern": r"(urn:lsid:([\w\-\.]+\.[\w\-\.]+)+:Image:\S+)|(Image:\S+)",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )


@dataclass
class LongAnnotation(NumericAnnotation):
    """
    A simple numerical annotation of type xsd:long.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    value: Optional[int] = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "required": True,
        },
    )


@dataclass
class StructuredAnnotations:
    """
    An unordered collection of annotation attached to objects in the OME data
    model.
    """

    class Meta:
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    xmlannotation: list[Xmlannotation] = field(
        default_factory=list,
        metadata={
            "name": "XMLAnnotation",
            "type": "Element",
        },
    )
    file_annotation: list[FileAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "FileAnnotation",
            "type": "Element",
        },
    )
    list_annotation: list[ListAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "ListAnnotation",
            "type": "Element",
        },
    )
    long_annotation: list[LongAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "LongAnnotation",
            "type": "Element",
        },
    )
    double_annotation: list[DoubleAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "DoubleAnnotation",
            "type": "Element",
        },
    )
    comment_annotation: list[CommentAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "CommentAnnotation",
            "type": "Element",
        },
    )
    boolean_annotation: list[BooleanAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "BooleanAnnotation",
            "type": "Element",
        },
    )
    timestamp_annotation: list[TimestampAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "TimestampAnnotation",
            "type": "Element",
        },
    )
    tag_annotation: list[TagAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "TagAnnotation",
            "type": "Element",
        },
    )
    term_annotation: list[TermAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "TermAnnotation",
            "type": "Element",
        },
    )
    map_annotation: list[MapAnnotation] = field(
        default_factory=list,
        metadata={
            "name": "MapAnnotation",
            "type": "Element",
        },
    )


@dataclass
class Ome:
    """The OME element is a container for all information objects accessible by
    OME.

    These information objects include descriptions of the imaging experiments
    and the people who perform them, descriptions of the microscope, the resulting
    images and how they were acquired, the analyses performed on those images,
    and the analysis results themselves.
    An OME file may contain any or all of this information.
    With the creation of the Metadata Only Companion OME-XML and Binary Only OME-TIFF files
    the top level OME node has changed slightly.
    It can EITHER:
    Contain all the previously expected elements
    OR:
    Contain a single BinaryOnly element that points at
    its Metadata Only Companion OME-XML file.

    :ivar rights:
    :ivar project:
    :ivar dataset:
    :ivar folder:
    :ivar experiment:
    :ivar plate:
    :ivar screen:
    :ivar experimenter:
    :ivar experimenter_group:
    :ivar instrument:
    :ivar image:
    :ivar structured_annotations:
    :ivar roi:
    :ivar binary_only: Pointer to an external metadata file. If this
        element is present, then no other metadata may be present in
        this file, i.e. this file is a place-holder.
    :ivar uuid: This unique identifier is used to keep track of multi
        part files. It allows the links between files to survive
        renaming. While OPTIONAL in the general case this is REQUIRED in
        a MetadataOnly Companion to a collection of BinaryOnly files.
    :ivar creator: This is the name of the creating application of the
        OME-XML and preferably its full version. e.g "CompanyName,
        SoftwareName, V2.6.3456" This is optional but we hope it will be
        set by applications writing out OME-XML from scratch.
    """

    class Meta:
        name = "OME"
        namespace = "http://www.openmicroscopy.org/Schemas/OME/2016-06"

    rights: Optional[Rights] = field(
        default=None,
        metadata={
            "name": "Rights",
            "type": "Element",
        },
    )
    project: list[Project] = field(
        default_factory=list,
        metadata={
            "name": "Project",
            "type": "Element",
        },
    )
    dataset: list[Dataset] = field(
        default_factory=list,
        metadata={
            "name": "Dataset",
            "type": "Element",
        },
    )
    folder: list[Folder] = field(
        default_factory=list,
        metadata={
            "name": "Folder",
            "type": "Element",
        },
    )
    experiment: list[Experiment] = field(
        default_factory=list,
        metadata={
            "name": "Experiment",
            "type": "Element",
        },
    )
    plate: list[Plate] = field(
        default_factory=list,
        metadata={
            "name": "Plate",
            "type": "Element",
        },
    )
    screen: list[Screen] = field(
        default_factory=list,
        metadata={
            "name": "Screen",
            "type": "Element",
        },
    )
    experimenter: list[Experimenter] = field(
        default_factory=list,
        metadata={
            "name": "Experimenter",
            "type": "Element",
        },
    )
    experimenter_group: list[ExperimenterGroup] = field(
        default_factory=list,
        metadata={
            "name": "ExperimenterGroup",
            "type": "Element",
        },
    )
    instrument: list[Instrument] = field(
        default_factory=list,
        metadata={
            "name": "Instrument",
            "type": "Element",
        },
    )
    image: list[Image] = field(
        default_factory=list,
        metadata={
            "name": "Image",
            "type": "Element",
        },
    )
    structured_annotations: Optional[StructuredAnnotations] = field(
        default=None,
        metadata={
            "name": "StructuredAnnotations",
            "type": "Element",
        },
    )
    roi: list[Roi] = field(
        default_factory=list,
        metadata={
            "name": "ROI",
            "type": "Element",
        },
    )
    binary_only: Optional["Ome.BinaryOnly"] = field(
        default=None,
        metadata={
            "name": "BinaryOnly",
            "type": "Element",
        },
    )
    uuid: Optional[str] = field(
        default=None,
        metadata={
            "name": "UUID",
            "type": "Attribute",
            "pattern": r"(urn:uuid:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})",
        },
    )
    creator: Optional[str] = field(
        default=None,
        metadata={
            "name": "Creator",
            "type": "Attribute",
        },
    )

    @dataclass
    class BinaryOnly:
        """
        :ivar metadata_file: Filename of the OME-XML metadata file for
            this binary data. If the file cannot be found, a search can
            be performed based on the UUID.
        :ivar uuid: The unique identifier of another OME-XML block whose
            metadata describes the binary data in this file. This UUID
            is considered authoritative regardless of mismatches in the
            filename.
        """

        metadata_file: Optional[str] = field(
            default=None,
            metadata={
                "name": "MetadataFile",
                "type": "Attribute",
                "required": True,
            },
        )
        uuid: Optional[str] = field(
            default=None,
            metadata={
                "name": "UUID",
                "type": "Attribute",
                "required": True,
                "pattern": r"(urn:uuid:[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12})",
            },
        )
