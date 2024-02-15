from utils.SwizzleUtils import *
from  IdentifySwizzles_x86_results import x86_swizzles
from  IdentifySwizzles_hvx_results import hvx_IdentifySwizzles as hvx_swizzles
from  IdentifySwizzles_arm_results import arm_swizzles




summarize_distinct_swizzles(hvx_swizzles, target_name = "hvx")
#summarize_distinct_swizzles(x86_swizzles, target_name = "x86")
#summarize_distinct_swizzles(arm_swizzles, target_name = "arm")
