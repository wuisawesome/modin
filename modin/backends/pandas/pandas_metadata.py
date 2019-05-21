# from modin import pandas as pd


class PandasMetaData:
    def __init__(self, dtypes, counts, mem_usage_deep, mem_usage_shallow):
        self.dtypes = dtypes
        self.counts = counts
        self.mem_usage_deep = mem_usage_deep
        self.mem_usage_shallow = mem_usage_shallow

    def copy(self):
        return PandasMetaData(
            dtypes=self.dtypes,
            counts=self.counts,
            mem_usage_deep=self.mem_usage_deep,
            mem_usage_shallow=self.mem_usage_shallow,
        )

    def __repr__(self):
        return (
            "Pandas QueryCompiler Metadata Cache: \ndtypes: %s\ncount: %s\nmem_usage_deep: %s\nmemusage_shallow: %s"
            % (self.dtypes, self.counts, self.mem_usage_deep, self.mem_usage_shallow)
        )
