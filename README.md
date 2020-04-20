# financial-analysis
Goal: explore security analysis, algorithmic trading strategies, and applications of ML to finance

File hierarchy:
- src /
  - data / ... houses datasets
  - dev / ... responsible for creating datasets
    - init / ... reading and pre-processing raw data
    - metrics / ... adds trading metrics and indicators to preprocessed data
  - static_models / ... manually configured strategies for algorithmic trading and asset analysis
    - momentum / ... momentum based strategies
    - mean_reversion / ... mean reversion based strategies
  - learned_models / ... ML based strategies for algorithmic trading and asset analysis
    - supervised / ... supervised ML algos
    - unsupervised / ... unsupervised ML algos
  - eval / ... performance evaluation of trading models using backtesting

Naming conventions, design patterns, other guidelines:
- files, methods named using snake_case
- classes named used CapitalCamelCase
- format raw dates as YYYYMMDD (ex, jan 31, 2000 is 20000131)
- only push head representations of datasets (<10mb) to remote repository
