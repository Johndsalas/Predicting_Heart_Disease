''' Code for exploration charts'''

import pandas
import matplotlib.pyplot as plt


def get_general_health(df):
    ''' Displays general health chart'''

    # get total rows for each health category
    tot = len(df) 
    etot = len(df[df.GeneralHealth == 'Excellent'])
    vtot = len(df[df.GeneralHealth == 'Very good'])
    gtot = len(df[df.GeneralHealth == 'Good'])
    ftot = len(df[df.GeneralHealth == 'Fair'])
    ptot = len(df[df.GeneralHealth == 'Poor'])
    
    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    eandh = len(df[(df.GeneralHealth == 'Excellent') & (df.HadHeartAttack == 'Yes')])
    vandh = len(df[(df.GeneralHealth == 'Very good') & (df.HadHeartAttack == 'Yes')])
    gandh = len(df[(df.GeneralHealth == 'Good') & (df.HadHeartAttack == 'Yes')])
    fandh = len(df[(df.GeneralHealth == 'Fair') & (df.HadHeartAttack == 'Yes')])
    pandh = len(df[(df.GeneralHealth == 'Poor') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    eave = round(eandh / etot,2) * 100
    vave = round(vandh / vtot, 2) * 100
    gave = round(gandh / gtot,2) * 100
    fave = round(fandh/ ftot,2) * 100
    pave = round(pandh / ptot,2) * 100

    # set values and hights
    vals = ['Overall',
            'Excellent',
            'Very Good',
            'Good',
            'Fair',
            'Poor']
     
    hights = [tave,
              eave,
              vave,
              gave,
              fave,
              pave]

    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Health Group How Who Had a Heart Attack')
    plt.show()


def get_physical_health_days(df):
    '''Displays physical health days chart'''

    # set values and hights
    vals = ['Overall',
            'Had Heart Attack',
            'No Heart Attack']
    
    hights = [df.PhysicalHealthDays.mean(),
              df[df.HadHeartAttack == 'Yes'].PhysicalHealthDays.mean(),
              df[df.HadHeartAttack == 'No'].PhysicalHealthDays.mean()]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Number of Poor Health Days In the Last 30 Days')
    plt.show()


def get_difficulty_dressing(df):
    '''Displays difficulties chart'''
    
    # get total rows for each health category
    tot = len(df) 
    difftot = len(df[df.DifficultyDressingBathing == 'Yes'])
    nodifftot = len(df[df.DifficultyDressingBathing == 'No'])

    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    diffandh = len(df[(df.DifficultyDressingBathing == 'Yes') & (df.HadHeartAttack == 'Yes')])
    nodiffandh = len(df[(df.DifficultyDressingBathing == 'No') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    diffave = round( diffandh / difftot, 2) * 100
    nodiffave = round( nodiffandh / nodifftot, 2) * 100

    # set values and hights
    vals = ['Overall',
            'Has Difficulty Dressing/Bathing',
            'No Difficulty Dressing/Bathing']
    
    hights = [tave,
              diffave,
              nodiffave]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Group How Who Had a Heart Attack')
    plt.show()


def get_difficulty_walking(df):
    '''Displays difficulties chart'''
    
    # get total rows for each health category
    tot = len(df) 
    difftot = len(df[df.DifficultyWalking == 'Yes'])
    nodifftot = len(df[df.DifficultyWalking == 'No'])

    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    diffandh = len(df[(df.DifficultyWalking == 'Yes') & (df.HadHeartAttack == 'Yes')])
    nodiffandh = len(df[(df.DifficultyWalking == 'No') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    diffave = round( diffandh / difftot, 2) * 100
    nodiffave = round( nodiffandh / nodifftot, 2) * 100

    # set values and hights
    vals = ['Overall',
            'Has Difficulty Walking',
            'No Difficulty Walking']
    
    hights = [tave,
              diffave,
              nodiffave]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Group How Who Had a Heart Attack')
    plt.show()


def get_difficulty_Errands(df):
    '''Displays difficulties chart'''
    
    # get total rows for each health category
    tot = len(df) 
    difftot = len(df[df.DifficultyErrands == 'Yes'])
    nodifftot = len(df[df.DifficultyErrands == 'No'])

    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    diffandh = len(df[(df.DifficultyErrands == 'Yes') & (df.HadHeartAttack == 'Yes')])
    nodiffandh = len(df[(df.DifficultyErrands == 'No') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    diffave = round( diffandh / difftot, 2) * 100
    nodiffave = round( nodiffandh / nodifftot, 2) * 100

    # set values and hights
    vals = ['Overall',
            'Difficulty with Errands',
            'No Difficulty with Errands']
    
    hights = [tave,
              diffave,
              nodiffave]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Group How Who Had a Heart Attack')
    plt.show()


def get_deaf(df):
    '''Displays difficulties chart'''
    
    # get total rows for each health category
    tot = len(df) 
    difftot = len(df[df.DeafOrHardOfHearing == 'Yes'])
    nodifftot = len(df[df.DeafOrHardOfHearing == 'No'])

    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    diffandh = len(df[(df.DeafOrHardOfHearing == 'Yes') & (df.HadHeartAttack == 'Yes')])
    nodiffandh = len(df[(df.DeafOrHardOfHearing == 'No') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    diffave = round( diffandh / difftot, 2) * 100
    nodiffave = round( nodiffandh / nodifftot, 2) * 100

    # set values and hights
    vals = ['Overall',
            'Deaf or Hard of Hearing',
            'Not Deaf or Hard of Hearing']
    
    hights = [tave,
              diffave,
              nodiffave]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Group How Who Had a Heart Attack')
    plt.show()


def get_blind(df):
    '''Displays difficulties chart'''
    
    # get total rows for each health category
    tot = len(df) 
    difftot = len(df[df.BlindOrVisionDifficulty == 'Yes'])
    nodifftot = len(df[df.BlindOrVisionDifficulty == 'No'])

    # get total rows for each health category that had a heart attach
    toth = len(df[df.HadHeartAttack == 'Yes'])
    diffandh = len(df[(df.BlindOrVisionDifficulty == 'Yes') & (df.HadHeartAttack == 'Yes')])
    nodiffandh = len(df[(df.BlindOrVisionDifficulty == 'No') & (df.HadHeartAttack == 'Yes')])

    # get percent of each category that has had a heart attack
    tave = round(toth / tot,2) * 100
    diffave = round( diffandh / difftot, 2) * 100
    nodiffave = round( nodiffandh / nodifftot, 2) * 100

    # set values and hights
    vals = ['Overall',
            'Has Difficulty Walking',
            'No Difficulty Walking']
    
    hights = [tave,
              diffave,
              nodiffave]
    
    # plot figure
    plt.figure(figsize=(16,6))
    plt.bar(vals, hights)
    plt.title(f'Percent of Each Group How Who Had a Heart Attack')
    plt.show()