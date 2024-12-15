function [net, testLabels, predictedLabels] = neuralnetwork(trainData, trainLabels)

    if ~iscategorical(trainLabels)
        uniqueLabels = unique(trainLabels);
        classNames = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'};
        trainLabels = categorical(trainLabels, uniqueLabels, classNames);
    end

    cv = cvpartition(size(trainData, 1), 'HoldOut', 0.1);
    indexTrain = training(cv);
    indexTest = test(cv);

    trainDataSplit = trainData(indexTrain, :);
    trainLabelsSplit = trainLabels(indexTrain);
    testData = trainData(indexTest, :);
    testLabels = trainLabels(indexTest);

    layers = [
        featureInputLayer(42)
        fullyConnectedLayer(64)
        reluLayer
        fullyConnectedLayer(32)
        reluLayer
        fullyConnectedLayer(numel(categories(trainLabels)))
        softmaxLayer
        classificationLayer
    ];

    options = trainingOptions('adam', ...
        'InitialLearnRate', 0.001, ...
        'MaxEpochs', 40, ...
        'MiniBatchSize', 32, ...
        'Shuffle', 'every-epoch', ...
        'Verbose', true, ...
        'Plots', 'training-progress');

    net = trainNetwork(trainDataSplit, trainLabelsSplit, layers, options);

    predictedLabels = classify(net, testData);
§
    predictedLabels = categorical(predictedLabels, categories(trainLabels));

    cm = confusionmat(testLabels, predictedLabels);
    disp('Confusion Matrix:');
    disp(cm);

    confusionchart(testLabels, predictedLabels, ...
        'Title', 'Confusion Matrix', ...
        'RowSummary', 'row-normalized', ...
        'ColumnSummary', 'off');

    save('new_NN.mat', 'net');
end
