#!/bin/sh
#SBATCH -A SEYEDAM_LAB
#SBATCH --cpus-per-task 1
#SBATCH --output=LDAs.out
#SBATCH --error=LDAs.err
#SBATCH --time=1:00:00
#SBATCH -J topyfic_paper
#SBATCH --mail-type=START,END
#SBATCH --partition=standard

for i in {0..99}
do
    scriptName=run_${i}
    curr=${scriptName}.sh
    echo '#!/bin/bash' > ${curr}
    echo '#SBATCH -A SEYEDAM_LAB' >> ${curr}
    echo '#SBATCH --cpus-per-task 10' >> ${curr}
    echo '#SBATCH --output=LDA-%J.out' >> ${curr}
    echo '#SBATCH --error=LDA-%J.err' >> ${curr}
    echo '#SBATCH --time=02:00:00' >> ${curr}
    echo '#SBATCH -J topyfic_paper_%J' >> ${curr}
    echo '#SBATCH --mail-type=START,END' >> ${curr}
    echo '#SBATCH --partition=standard' >> ${curr}
    
    echo "python3 topyfic.py 5 ${i}" >> ${curr}
    
    chmod +x ${curr}
    sbatch ${scriptName}.sh
    
done

