from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

engine=create_engine('postgresql://postgres.slrnaagetxjwecbbgekk:MWy6?9htv*kWgNm@aws-0-us-west-1.pooler.supabase.com:6543/asoahocre',
    echo=True
)

Base=declarative_base()

Session=sessionmaker()