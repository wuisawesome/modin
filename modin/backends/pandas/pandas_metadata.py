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


def from_pandas(df):
    dtypes = df.dtypes
    counts = df.count()
    mem_usage_deep = df.memory_usage(index=False, deep=True)
    mem_usage_shallow = df.memory_usage(index=False, deep=False)
    return PandasMetaData(
        dtypes=dtypes,
        counts=counts,
        mem_usage_deep=mem_usage_deep,
        mem_usage_shallow=mem_usage_shallow,
    )
